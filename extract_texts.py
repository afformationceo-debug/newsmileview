#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
extract_texts.py - 한국어 텍스트 추출기 v2
8개 HTML 파일에서 모든 한국어 텍스트를 추출하여 translations/ko/ 에 JSON으로 저장
"""

import os
import json
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "translations", "ko")
os.makedirs(OUTPUT_DIR, exist_ok=True)

PAGES = [
    "index",
    "invisalign",
    "ortho",
    "laminate",
    "whitening",
    "implant",
    "prosthetics",
    "introduction",
]

KOREAN_RE = re.compile(r"[가-힣ㄱ-ㅎㅏ-ㅣ]")


def extract_from_file(filepath):
    """라인별로 모든 한국어 포함 항목 추출"""
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    results = []
    index = 0
    seen_texts = set()

    for lineno, raw_line in enumerate(lines, start=1):
        line = raw_line.rstrip("\n")
        if not KOREAN_RE.search(line):
            continue

        # 태그 이름 추측
        tag_match = re.match(r"\s*<([a-zA-Z][a-zA-Z0-9-]*)", line)
        tag_name = tag_match.group(1) if tag_match else "text"

        # ── 1. 메타 태그 content ──────────────────────────────
        meta_m = re.search(r'<meta[^>]+content=["\']([^"\']*)["\']', line)
        if meta_m:
            val = meta_m.group(1).strip()
            if KOREAN_RE.search(val) and val not in seen_texts:
                seen_texts.add(val)
                index += 1
                # property 또는 name 속성 추출
                name_m = re.search(r'(?:name|property)=["\']([^"\']+)["\']', line)
                meta_name = name_m.group(1) if name_m else "meta"
                results.append({
                    "key": f"meta_{index}_{re.sub(r'[^a-z0-9]', '_', meta_name.lower())}",
                    "text": val,
                    "location": f"line:{lineno}, meta[{meta_name}]",
                    "context": "meta"
                })

        # ── 2. <title> ────────────────────────────────────────
        title_m = re.search(r"<title>([^<]+)</title>", line)
        if title_m:
            val = title_m.group(1).strip()
            if KOREAN_RE.search(val) and val not in seen_texts:
                seen_texts.add(val)
                index += 1
                results.append({
                    "key": f"title_{index}",
                    "text": val,
                    "location": f"line:{lineno}, tag:title",
                    "context": "title"
                })

        # ── 3. HTML 속성 (alt, placeholder, title, aria-label) ─
        ATTR_NAMES = ["alt", "placeholder", "title", "aria-label", "aria-placeholder"]
        for attr in ATTR_NAMES:
            attr_pattern = re.compile(rf'{attr}=["\']([^"\']*)["\']', re.IGNORECASE)
            for m in attr_pattern.finditer(line):
                val = m.group(1).strip()
                if KOREAN_RE.search(val) and val not in seen_texts:
                    seen_texts.add(val)
                    index += 1
                    results.append({
                        "key": f"attr_{index}_{tag_name}_{attr.replace('-', '_')}",
                        "text": val,
                        "location": f"line:{lineno}, tag:{tag_name}[{attr}]",
                        "context": f"attr:{attr}"
                    })

        # ── 4. data-* 속성 ───────────────────────────────────
        data_attr_pattern = re.compile(r'(data-[a-z0-9-]+)=["\']([^"\']*)["\']', re.IGNORECASE)
        for m in data_attr_pattern.finditer(line):
            attr_name = m.group(1)
            val = m.group(2).strip()
            if KOREAN_RE.search(val) and val not in seen_texts:
                seen_texts.add(val)
                index += 1
                results.append({
                    "key": f"data_{index}_{tag_name}_{attr_name.replace('-', '_')}",
                    "text": val,
                    "location": f"line:{lineno}, tag:{tag_name}[{attr_name}]",
                    "context": f"attr:{attr_name}"
                })

        # ── 5. 태그 내부 텍스트 ─────────────────────────────
        # 인라인 태그 포함 텍스트 추출 (내부 태그 제거 후)
        # 먼저 script/style 라인 건너뛰기
        if re.search(r"<(?:script|style)", line, re.IGNORECASE):
            # script/style 내부는 별도 처리
            pass
        else:
            # 태그 제거 후 텍스트 추출
            text_only = re.sub(r"<[^>]+>", " ", line).strip()
            text_only = re.sub(r"\s+", " ", text_only).strip()
            if text_only and KOREAN_RE.search(text_only) and text_only not in seen_texts:
                seen_texts.add(text_only)
                index += 1
                results.append({
                    "key": f"text_{index}_{tag_name}",
                    "text": text_only,
                    "location": f"line:{lineno}, tag:{tag_name}",
                    "context": "text"
                })

        # ── 6. CSS content 속성 ──────────────────────────────
        css_content_m = re.search(r"content\s*:\s*[\"']([^\"']*)[\"']", line)
        if css_content_m:
            val = css_content_m.group(1).strip()
            if KOREAN_RE.search(val) and val not in seen_texts:
                seen_texts.add(val)
                index += 1
                results.append({
                    "key": f"css_content_{index}",
                    "text": val,
                    "location": f"line:{lineno}, css:content",
                    "context": "css_content"
                })

        # ── 7. JS 문자열 리터럴 ──────────────────────────────
        # script 태그 내부는 script 블록 전체를 별도 처리 필요
        # 여기서는 인라인 JS (onclick 등) 처리
        inline_js_attrs = ["onclick", "onchange", "oninput", "data-text"]
        for attr in inline_js_attrs:
            js_m = re.search(rf'{attr}=["\']([^"\']*)["\']', line)
            if js_m:
                val = js_m.group(1).strip()
                if KOREAN_RE.search(val) and val not in seen_texts:
                    seen_texts.add(val)
                    index += 1
                    results.append({
                        "key": f"js_{index}_{attr.replace('-', '_')}",
                        "text": val,
                        "location": f"line:{lineno}, js:{attr}",
                        "context": "javascript"
                    })

    # ── 8. <script> 블록 전체 스캔 ───────────────────────────
    with open(filepath, "r", encoding="utf-8") as f:
        full_content = f.read()

    for script_match in re.finditer(r"<script(?:\s[^>]*)?>(.+?)</script>", full_content, re.DOTALL):
        # src 속성 있으면 외부 스크립트 스킵
        script_tag = full_content[script_match.start():script_match.start() + 100]
        if "src=" in script_tag:
            continue
        script_body = script_match.group(1)
        line_offset = full_content[:script_match.start()].count("\n") + 1

        string_patterns = [
            r"'([^'\n]*[가-힣][^'\n]*)'",
            r'"([^"\n]*[가-힣][^"\n]*)"',
            r'`([^`]*[가-힣][^`]*)`',
        ]
        for pat in string_patterns:
            for m in re.finditer(pat, script_body):
                val = m.group(1).strip()
                if val and KOREAN_RE.search(val) and val not in seen_texts:
                    seen_texts.add(val)
                    index += 1
                    js_line = line_offset + script_body[:m.start()].count("\n")
                    results.append({
                        "key": f"js_str_{index}",
                        "text": val,
                        "location": f"line:{js_line}, js:string",
                        "context": "javascript"
                    })

    return results


def main():
    total = 0
    for page in PAGES:
        filepath = os.path.join(BASE_DIR, f"{page}.html")
        if not os.path.exists(filepath):
            print(f"[SKIP] {page}.html not found")
            continue

        items = extract_from_file(filepath)
        out_path = os.path.join(OUTPUT_DIR, f"{page}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=2)

        print(f"[OK] {page}.html -> {len(items)} items -> translations/ko/{page}.json")
        total += len(items)

    print(f"\nTotal: {total} Korean texts extracted")
    print(f"Output: translations/ko/")


if __name__ == "__main__":
    main()
