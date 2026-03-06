import json

data = [
  {
    "key": "title_1",
    "text": "치아교정 | 스마일뷰치과의원",
    "translated": "牙齒矯正 | SMILEVIEW牙醫診所",
    "location": "line:6, tag:title",
    "context": "title"
  },
  {
    "key": "text_2_li",
    "text": "스마일뷰치과",
    "translated": "SMILEVIEW牙醫診所",
    "location": "line:962, tag:li",
    "context": "text"
  },
  {
    "key": "text_3_li",
    "text": "인비절라인",
    "translated": "INVISALIGN",
    "location": "line:963, tag:li",
    "context": "text"
  },
  {
    "key": "text_4_li",
    "text": "치아교정",
    "translated": "牙齒矯正",
    "location": "line:964, tag:li",
    "context": "text"
  },
  {
    "key": "text_5_li",
    "text": "치아미백",
    "translated": "牙齒美白",
    "location": "line:965, tag:li",
    "context": "text"
  },
  {
    "key": "text_6_li",
    "text": "원데이 라미네이트",
    "translated": "單日瓷貼片",
    "location": "line:966, tag:li",
    "context": "text"
  },
  {
    "key": "text_7_li",
    "text": "수면 임플란트",
    "translated": "舒眠植牙",
    "location": "line:967, tag:li",
    "context": "text"
  },
  {
    "key": "text_8_li",
    "text": "보철치료",
    "translated": "補綴治療",
    "location": "line:968, tag:li",
    "context": "text"
  },
  {
    "key": "text_9_a",
    "text": "한국어 (KO)",
    "translated": "韓語 (KO)",
    "location": "line:976, tag:a",
    "context": "text"
  },
  {
    "key": "text_10_a",
    "text": "예약하기",
    "translated": "立即預約",
    "location": "line:981, tag:a",
    "context": "text"
  },
  {
    "key": "text_11_li",
    "text": "병원소개",
    "translated": "診所介紹",
    "location": "line:992, tag:li",
    "context": "text"
  },
  {
    "key": "text_12_a",
    "text": "온라인 예약",
    "translated": "線上預約",
    "location": "line:1001, tag:a",
    "context": "text"
  },
  {
    "key": "text_13_text",
    "text": "치아와 턱의 비정상적인 위치를 교정하여",
    "translated": "矯正牙齒與下顎的異常位置，",
    "location": "line:1019, tag:text",
    "context": "text"
  },
  {
    "key": "text_14_text",
    "text": "미소와 턱의 기능을 향상시키는 치료과정입니다.",
    "translated": "改善笑容與咬合功能的治療過程。",
    "location": "line:1020, tag:text",
    "context": "text"
  },
  {
    "key": "text_15_text",
    "text": "치아의 이상적인 위치와 상태를 재조정하여",
    "translated": "重新調整牙齒至理想位置與狀態，",
    "location": "line:1023, tag:text",
    "context": "text"
  },
  {
    "key": "text_16_text",
    "text": "아름다운 스마일 라인과 건강한 구강을 선사합니다.",
    "translated": "打造美麗的笑容曲線與健康的口腔環境。",
    "location": "line:1024, tag:text",
    "context": "text"
  },
  {
    "key": "text_17_p",
    "text": "치아교정 솔루션",
    "translated": "SMILEVIEW SOLUTIONS",
    "location": "line:1048, tag:p",
    "context": "text"
  },
  {
    "key": "text_18_h2",
    "text": "치아교정이란?",
    "translated": "什麼是牙齒矯正？",
    "location": "line:1082, tag:h2",
    "context": "text"
  },
  {
    "key": "text_19_text",
    "text": "치아교정은 치아와 턱의 비정상적인 위치나 교합 문제를 전문 교정 장치를 이용하여 바르게 교정하는 치료과정입니다. 턱과 치아의 위치를 조정하여 교합과 치아의 기능을 안정시키고, 변화된 턱의 길이와 위치를 조절하여 턱과 안면 근육의 균형을 맞출 수 있습니다. 아름다운 스마일 라인과 함께 건강한 구강 기능을 되찾을 수 있습니다.",
    "translated": "牙齒矯正是利用專業矯正裝置，矯正牙齒與下顎位置異常或咬合問題的治療過程。透過調整顎骨與牙齒位置，穩定咬合與牙齒功能，同時調整顎骨長度與位置，使顎骨與顏面肌肉達到平衡。讓您重拾健康的口腔功能，同時擁有美麗的笑容曲線。",
    "location": "line:1084, tag:text",
    "context": "text"
  },
  {
    "key": "text_20_b",
    "text": "교정유형",
    "translated": "矯正類型",
    "location": "line:1090, tag:b",
    "context": "text"
  },
  {
    "key": "text_21_span",
    "text": "선수술 교정, 주걱턱 교정, 안면비대칭 교정, 돌출입 교정, 부분교정, 설측교정 등",
    "translated": "術前矯正、戽斗矯正、顏面不對稱矯正、暴牙矯正、局部矯正、舌側矯正等",
    "location": "line:1091, tag:span",
    "context": "text"
  },
  {
    "key": "text_22_h2",
    "text": "시술 정보",
    "translated": "療程資訊",
    "location": "line:1105, tag:h2",
    "context": "text"
  },
  {
    "key": "text_23_div",
    "text": "시술시간",
    "translated": "療程時間",
    "location": "line:1109, tag:div",
    "context": "text"
  },
  {
    "key": "text_24_div",
    "text": "약 1~2시간(첫 방문)",
    "translated": "約 1～2 小時（初診）",
    "location": "line:1110, tag:div",
    "context": "text"
  },
  {
    "key": "text_25_div",
    "text": "마취방법",
    "translated": "麻醉方式",
    "location": "line:1114, tag:div",
    "context": "text"
  },
  {
    "key": "text_26_div",
    "text": "불필요",
    "translated": "不需要",
    "location": "line:1115, tag:div",
    "context": "text"
  },
  {
    "key": "text_27_div",
    "text": "교정기간",
    "translated": "矯正期間",
    "location": "line:1119, tag:div",
    "context": "text"
  },
  {
    "key": "text_28_div",
    "text": "12~24개월",
    "translated": "12～24 個月",
    "location": "line:1120, tag:div",
    "context": "text"
  },
  {
    "key": "text_29_div",
    "text": "내원주기",
    "translated": "回診週期",
    "location": "line:1124, tag:div",
    "context": "text"
  },
  {
    "key": "text_30_div",
    "text": "3~4주",
    "translated": "3～4 週",
    "location": "line:1125, tag:div",
    "context": "text"
  },
  {
    "key": "text_31_h2",
    "text": "선수술 교정이란?",
    "translated": "什麼是術前矯正？",
    "location": "line:1136, tag:h2",
    "context": "text"
  },
  {
    "key": "text_32_h3",
    "text": "수술 먼저, 교정은 나중에",
    "translated": "先手術，再矯正",
    "location": "line:1139, tag:h3",
    "context": "text"
  },
  {
    "key": "text_33_text",
    "text": "선수술 교정은 기존의 '교정 → 수술' 순서를 역전시켜, 턱수술을 먼저 시행한 뒤 교정 치료를 진행하는 방법입니다. 수술을 통해 골격적 부조화를 먼저 해결하므로 외모 개선이 빠르게 이루어지며, 비정상적인 골격이 정상 골격으로 바뀌면서 심미적 만족감을 조기에 얻을 수 있습니다.",
    "translated": "術前矯正顛覆傳統「矯正→手術」的順序，改為先進行顎骨手術，再接受矯正治療。由於先以手術解決骨骼不協調的問題，外觀改善快速，異常骨骼轉變為正常骨骼後，能夠提早獲得令人滿意的美觀效果。",
    "location": "line:1142, tag:text",
    "context": "text"
  },
  {
    "key": "text_34_text",
    "text": "수술 후 변화된 턱과 치아의 위치를 정밀하게 재조정하여 교합과 치아의 기능을 안정시키고 회복시키는 것이 핵심 목적이며, 전통적인 교정-수술 방식 대비 전체 치료 기간을 단축할 수 있는 장점이 있습니다.",
    "translated": "其核心目標在於精密重新調整手術後改變的顎骨與牙齒位置，穩定並恢復咬合與牙齒功能。相較於傳統矯正後手術的方式，整體療程時間可大幅縮短。",
    "location": "line:1145, tag:text",
    "context": "text"
  },
  {
    "key": "text_35_span",
    "text": "Surgery First 선수술 우선",
    "translated": "Surgery First 術前矯正優先",
    "location": "line:1149, tag:span",
    "context": "text"
  },
  {
    "key": "attr_36_img_alt",
    "text": "선수술 교정",
    "translated": "術前矯正",
    "location": "line:1151, tag:img[alt]",
    "context": "attr:alt"
  },
  {
    "key": "attr_37_img_alt",
    "text": "수술 전 정밀 분석",
    "translated": "手術前精密分析",
    "location": "line:1159, tag:img[alt]",
    "context": "attr:alt"
  },
  {
    "key": "text_38_p",
    "text": "3D CT와 구강 스캔을 통해 골격 및 치아 상태를 정밀하게 분석하고, 환자의 얼굴 형태와 교합 상태를 종합적으로 평가하여 최적의 수술 계획을 수립합니다.",
    "translated": "透過 3D CT 與口腔掃描精密分析骨骼及牙齒狀況，綜合評估患者的臉型與咬合狀態，制定最佳手術計畫。",
    "location": "line:1164, tag:p",
    "context": "text"
  },
  {
    "key": "attr_39_img_alt",
    "text": "수술 직후",
    "translated": "手術後即刻",
    "location": "line:1171, tag:img[alt]",
    "context": "attr:alt"
  },
  {
    "key": "text_40_p",
    "text": "골격적 부조화를 해결하고 심미적 개선의 기반을 마련하는 단계입니다. 수술을 통해 비정상적인 골격이 정상 위치로 이동하여 외모 개선이 빠르게 나타납니다.",
    "translated": "此階段解決骨骼不協調問題，為外觀改善奠定基礎。透過手術將異常骨骼移至正常位置，外觀改善效果迅速顯現。",
    "location": "line:1176, tag:p",
    "context": "text"
  },
  {
    "key": "attr_41_img_alt",
    "text": "수술 후 교정 중",
    "translated": "手術後矯正中",
    "location": "line:1183, tag:img[alt]",
    "context": "attr:alt"
  },
  {
    "key": "text_42_p",
    "text": "변화된 턱 위치에 맞춰 치아 교합을 정밀하게 조정하는 과정입니다. 교정 장치를 통해 치아를 이상적인 위치로 이동시켜 안정적인 교합을 달성합니다.",
    "translated": "依據改變後的顎骨位置精密調整牙齒咬合的過程。透過矯正裝置將牙齒移至理想位置，達成穩定的咬合。",
    "location": "line:1188, tag:p",
    "context": "text"
  },
  {
    "key": "attr_43_img_alt",
    "text": "수술 후 교정 완료",
    "translated": "手術後矯正完成",
    "location": "line:1195, tag:img[alt]",
    "context": "attr:alt"
  },
  {
    "key": "text_44_p",
    "text": "안정된 교합과 아름다운 스마일 라인을 완성하는 최종 단계입니다. 유지장치를 통해 교정 결과가 오랫동안 유지될 수 있도록 관리합니다.",
    "translated": "完成穩定咬合與美麗笑容曲線的最終階段。透過保持器管理，確保矯正成果長期維持。",
    "location": "line:1200, tag:p",
    "context": "text"
  },
  {
    "key": "text_45_h2",
    "text": "스마일뷰 교정의 장점",
    "translated": "SMILEVIEW 矯正的優勢",
    "location": "line:1212, tag:h2",
    "context": "text"
  },
  {
    "key": "text_46_h3",
    "text": "빠른 심미적 개선",
    "translated": "快速改善外觀美感",
    "location": "line:1219, tag:h3",
    "context": "text"
  },
  {
    "key": "text_47_p",
    "text": "수술을 먼저 시행하여 외모 개선이 빠르게 이루어지며, 정상 골격으로의 변화를 통해 조기에 심미적 만족감을 경험할 수 있습니다.",
    "translated": "先進行手術使外觀快速改善，透過骨骼恢復正常，能提早感受到令人滿意的美觀效果。",
    "location": "line:1220, tag:p",
    "context": "text"
  },
  {
    "key": "text_48_h3",
    "text": "기능적 교합 회복",
    "translated": "恢復功能性咬合",
    "location": "line:1225, tag:h3",
    "context": "text"
  },
  {
    "key": "text_49_p",
    "text": "올바른 저작 기능과 턱 관절의 균형을 되찾아 전반적인 구강 건강을 향상시키고 안정적인 교합을 달성합니다.",
    "translated": "找回正確的咀嚼功能與顳顎關節平衡，全面提升口腔健康，達成穩定的咬合。",
    "location": "line:1226, tag:p",
    "context": "text"
  },
  {
    "key": "text_50_h3",
    "text": "교정과 전문의 협진",
    "translated": "矯正專科醫師跨科協作",
    "location": "line:1231, tag:h3",
    "context": "text"
  },
  {
    "key": "text_51_p",
    "text": "수술 계획부터 세심한 분析이 필요하기에, 교정과 의료진과의 긴밀한 협진을 통해 최적의 치료 결과를 도출합니다.",
    "translated": "從手術計畫開始便需要縝密的分析，透過矯正科醫療團隊的緊密協作，導出最佳的治療成果。",
    "location": "line:1232, tag:p",
    "context": "text"
  },
  {
    "key": "text_52_h3",
    "text": "체계적 사후관리",
    "translated": "系統性術後管理",
    "location": "line:1237, tag:h3",
    "context": "text"
  },
  {
    "key": "text_53_p",
    "text": "유지장치 관리와 정기 검진을 통해 교정 결과가 오랫동안 안정적으로 유지될 수 있도록 체계적인 사후관리를 제공합니다.",
    "translated": "透過保持器管理與定期回診，提供系統性的術後照護，確保矯正成果長期穩定維持。",
    "location": "line:1238, tag:p",
    "context": "text"
  },
  {
    "key": "text_54_h2",
    "text": "양악수술과 함께하는 교정 치료",
    "translated": "結合雙顎手術的矯正治療",
    "location": "line:1248, tag:h2",
    "context": "text"
  },
  {
    "key": "text_55_p",
    "text": "양악수술은 위턱과 아래턱의 골격 및 치아의 부정교합을 치료하고, 심미적인 얼굴 골격과 정상적인 교합을 얻고자 하는 수술입니다. 각 교정 유형을 클릭하여 자세한 정보를 확인하세요.",
    "translated": "雙顎手術是針對上下顎骨架及牙齒錯咬合進行治療，以獲得美觀臉型骨架與正常咬合為目標的外科手術。請點選各矯正類型，查看詳細資訊。",
    "location": "line:1250, tag:p",
    "context": "text"
  },
  {
    "key": "text_56_button",
    "text": "주걱턱 교정",
    "translated": "戽斗矯正",
    "location": "line:1253, tag:button",
    "context": "text"
  },
  {
    "key": "text_57_button",
    "text": "안면비대칭 교정",
    "translated": "顏面不對稱矯正",
    "location": "line:1254, tag:button",
    "context": "text"
  },
  {
    "key": "text_58_button",
    "text": "돌출입 교정",
    "translated": "暴牙矯正",
    "location": "line:1255, tag:button",
    "context": "text"
  },
  {
    "key": "text_59_h3",
    "text": "아래턱 돌출로 인한 주걱턱 교정",
    "translated": "因下顎前突引起的戽斗矯正",
    "location": "line:1277, tag:h3",
    "context": "text"
  },
  {
    "key": "text_60_p",
    "text": "아래턱 성장이 과도하거나 위턱 성장이 부족해 아래턱이 돌출된 경우 진행하는 교정입니다. 골격적 부조화를 해결하여 얼굴 균형과 정상적인 교합을 회복시킵니다.",
    "translated": "適用於下顎過度生長或上顎發育不足導致下顎前突的情況。透過解決骨骼不協調，恢復臉部均衡與正常咬合。",
    "location": "line:1278, tag:p",
    "context": "text"
  },
  {
    "key": "text_61_a",
    "text": "자세히 보기",
    "translated": "了解更多",
    "location": "line:1279, tag:a",
    "context": "text"
  },
  {
    "key": "text_62_h3",
    "text": "좌우 균형을 되찾는 안면비대칭 교정",
    "translated": "找回左右平衡的顏面不對稱矯正",
    "location": "line:1302, tag:h3",
    "context": "text"
  },
  {
    "key": "text_63_p",
    "text": "얼굴의 상하 길이 혹은 좌우 대칭의 균형이 맞지 않을 때 진행하는 교정입니다. 턱의 비대칭을 교정하여 균형 잡힌 얼굴 라인과 안정적인 교합을 달성합니다.",
    "translated": "適用於臉部上下長度或左右對稱比例失衡的情況。透過矯正顎骨不對稱，達成均衡的臉部輪廓與穩定的咬合。",
    "location": "line:1303, tag:p",
    "context": "text"
  },
  {
    "key": "text_64_h3",
    "text": "자연스러운 옆모습을 위한 돌출입 교정",
    "translated": "打造自然側臉輪廓的暴牙矯正",
    "location": "line:1327, tag:h3",
    "context": "text"
  },
  {
    "key": "text_65_p",
    "text": "코 끝이나 턱 끝에 비해 입이 앞으로 돌출되어 옆모습 개선이 필요한 경우 진행하는 교정입니다. E-line을 개선하고 자연스러운 입술 라인을 되찾아 드립니다.",
    "translated": "適用於相較於鼻尖或下巴末端，嘴唇向前突出、需要改善側臉輪廓的情況。改善 E-line，讓您找回自然的唇部線條。",
    "location": "line:1328, tag:p",
    "context": "text"
  },
  {
    "key": "text_66_p",
    "text": "아래턱 성장이 과도하거나 위턱 성장이 상대적으로 부족하여 아래턱이 튀어나온 경우 진행하는 교정으로, 골격적 부조화를 해결하여 얼굴 균형과 정상적인 교합을 회복시킵니다.",
    "translated": "適用於下顎過度生長或上顎相對發育不足導致下顎突出的矯正治療，透過解決骨骼不協調，恢復臉部均衡與正常咬合。",
    "location": "line:1343, tag:p",
    "context": "text"
  },
  {
    "key": "text_67_h3",
    "text": "아래턱 돌출로 인한 얼굴 불균형 개선",
    "translated": "改善因下顎前突造成的臉部不均衡",
    "location": "line:1362, tag:h3",
    "context": "text"
  },
  {
    "key": "text_68_p",
    "text": "주걱턱(하악전돌증)은 아래턱이 위턱보다 앞으로 나와 있는 상태로, 옆에서 보았을 때 아래턱이 돌출되어 보이고 정면에서는 얼굴이 길어 보이는 특징이 있습니다. 저작 기능의 저하뿐 아니라 발음 문제, 턱관절 장애를 동반할 수 있어 적극적인 교정이 필요합니다.",
    "translated": "戽斗（下顎前突症）是指下顎比上顎更向前突出的狀態，從側面看下顎明顯前突，從正面看臉型較長。除了咀嚼功能下降外，還可能伴隨發音問題及顳顎關節障礙，需要積極進行矯正治療。",
    "location": "line:1363, tag:p",
    "context": "text"
  },
  {
    "key": "text_69_h3",
    "text": "이런 분들에게 필요합니다",
    "translated": "適合以下情況的患者",
    "location": "line:1370, tag:h3",
    "context": "text"
  },
  {
    "key": "text_70_p",
    "text": "아래턱이 위턱보다 앞으로 나온 경우",
    "translated": "下顎比上顎更向前突出的情況",
    "location": "line:1375, tag:p",
    "context": "text"
  },
  {
    "key": "text_71_p",
    "text": "얼굴이 길어 인상이 강해보이거나 나이가 들어 보이는 경우",
    "translated": "因臉型較長而顯得表情強硬或看起來較老的情況",
    "location": "line:1379, tag:p",
    "context": "text"
  },
  {
    "key": "text_72_p",
    "text": "위아래 치아가 거꾸로 물려 저작 효율이 떨어지는 경우",
    "translated": "上下牙齒反咬導致咀嚼效率下降的情況",
    "location": "line:1383, tag:p",
    "context": "text"
  },
  {
    "key": "text_73_p",
    "text": "얼굴의 상하 길이 혹은 좌우 대칭의 균형이 맞지 않을 때 진행하는 교정으로, 턱의 비대칭을 교정하여 균형 잡힌 얼굴 라인과 안정적인 교합을 동시에 달성합니다.",
    "translated": "針對臉部上下長度或左右對稱比例失衡的矯正治療，透過矯正顎骨不對稱，同時達成均衡的臉部輪廓與穩定的咬合。",
    "location": "line:1396, tag:p",
    "context": "text"
  },
  {
    "key": "text_74_h3",
    "text": "좌우 균형을 되찾는 안면 대칭 교정",
    "translated": "找回左右平衡的顏面對稱矯正",
    "location": "line:1401, tag:h3",
    "context": "text"
  },
  {
    "key": "text_75_p",
    "text": "안면비대칭은 위턱 또는 아래턱의 좌우 길이가 다르거나, 턱이 한쪽으로 치우쳐 얼굴의 정중선이 어긋나는 상태입니다. 심미적 문제뿐 아니라 한쪽으로 편중된 저작 습관, 턱관절 통증, 치아 정중앙선의 불일치 등 기능적 문제를 동반할 수 있습니다.",
    "translated": "顏面不對稱是指上顎或下顎左右長度不同，或顎骨偏向一側導致臉部中線偏移的狀態。除了外觀問題外，還可能伴隨偏側咀嚼習慣、顳顎關節疼痛、牙齒中線不一致等功能性問題。",
    "location": "line:1402, tag:p",
    "context": "text"
  },
  {
    "key": "text_76_p",
    "text": "위턱의 좌우 길이가 맞지 않는 경우",
    "translated": "上顎左右長度不對稱的情況",
    "location": "line:1428, tag:p",
    "context": "text"
  },
  {
    "key": "text_77_p",
    "text": "아래턱의 좌우 대칭이 맞지 않는 경우",
    "translated": "下顎左右對稱失衡的情況",
    "location": "line:1432, tag:p",
    "context": "text"
  },
  {
    "key": "text_78_p",
    "text": "치아의 정중앙선이 위아래 치아끼리 많이 어긋난 경우",
    "translated": "上下牙齒中線明顯偏移不一致的情況",
    "location": "line:1436, tag:p",
    "context": "text"
  },
  {
    "key": "text_79_p",
    "text": "옆에서 보았을 때 코 끝이나 턱 끝에 비해 입이 앞으로 돌출된 경우 진행하는 교정으로, 옆모습의 E-line을 개선하고 자연스러운 입술 라인을 되찾아 드립니다.",
    "translated": "針對從側面看相較於鼻尖或下巴末端嘴唇明顯前突的矯正治療，改善側臉的 E-line，讓您找回自然的唇部線條。",
    "location": "line:1449, tag:p",
    "context": "text"
  },
  {
    "key": "text_80_h3",
    "text": "자연스러운 옆모습을 위한 돌출입 개선",
    "translated": "打造自然側臉輪廓的暴牙改善",
    "location": "line:1468, tag:h3",
    "context": "text"
  },
  {
    "key": "text_81_p",
    "text": "돌출입은 치아나 치조골이 앞으로 돌출되어 입이 나와 보이는 상태로, 입을 다물기 어렵거나 무의식적으로 입이 벌어지는 증상을 동반할 수 있습니다. 긴 얼굴, 안면비대칭, 잇몸과다노출(거미스마일) 등을 동반하는 경우가 많으며, 정확한 진단을 통해 개인에 맞는 최적의 교정 방법을 적용합니다.",
    "translated": "暴牙是指牙齒或齒槽骨向前突出導致嘴唇外凸的狀態，可能伴隨嘴巴難以完全閉合或無意識張口的症狀。常合併長臉型、顏面不對稱、牙齦外露過多（露齦笑）等情況，透過精確診斷，為每位患者制定最適合的矯正方案。",
    "location": "line:1469, tag:p",
    "context": "text"
  },
  {
    "key": "text_82_p",
    "text": "긴 얼굴을 동반한 돌출입의 경우",
    "translated": "合併長臉型的暴牙情況",
    "location": "line:1481, tag:p",
    "context": "text"
  },
  {
    "key": "text_83_p",
    "text": "안면비대칭을 동반한 돌출입의 경우",
    "translated": "合併顏面不對稱的暴牙情況",
    "location": "line:1485, tag:p",
    "context": "text"
  },
  {
    "key": "text_84_p",
    "text": "잇몸과다노출을 동반한 돌출입의 경우",
    "translated": "合併牙齦外露過多的暴牙情況",
    "location": "line:1489, tag:p",
    "context": "text"
  },
  {
    "key": "text_85_h2",
    "text": "자주 묻는 질문",
    "translated": "常見問題",
    "location": "line:1500, tag:h2",
    "context": "text"
  },
  {
    "key": "text_86_span",
    "text": "선수술 교정이란 무엇인가요?",
    "translated": "什麼是術前矯正？",
    "location": "line:1507, tag:span",
    "context": "text"
  },
  {
    "key": "text_87_strong",
    "text": "A. 선수술 교정은 턱수술을 먼저 시행한 뒤 교정 치료를 진행하는 방법입니다. 수술을 통해 골격적 부조화를 먼저 해결하므로 외모 개선이 빠르게 이루어지며, 비정상적인 골격이 정상 골격으로 바뀌면서 심미적 만족감을 조기에 얻을 수 있습니다. 수술 후 변화된 턱과 치아의 위치를 정밀하게 재조정하여 교합과 치아의 기능을 안정시키고 회복시키는 것이 핵심 목적입니다.",
    "translated": "A. 術前矯正是先進行顎骨手術，再接受矯正治療的方法。由於先以手術解決骨骼不協調問題，外觀改善迅速，骨骼由異常轉變為正常後，能提早獲得令人滿意的美觀效果。其核心目標在於精密重新調整手術後改變的顎骨與牙齒位置，穩定並恢復咬合與牙齒功能。",
    "location": "line:1511, tag:strong",
    "context": "text"
  },
  {
    "key": "text_88_span",
    "text": "양악수술 후 교정이 꼭 필요한가요?",
    "translated": "雙顎手術後一定需要矯正嗎？",
    "location": "line:1517, tag:span",
    "context": "text"
  },
  {
    "key": "text_89_strong",
    "text": "A. 양악수술은 골격적 기형을 해결할 수 있는 수술 방법이며, 수술 후 골격의 위치를 올바른 위치로 재조정하면 치아의 맞물림이 변할 수 있습니다. 따라서 양악수술 후에는 치아 교정이 필요할 수 있으며, 수술과 교정을 협진하여 진행함으로써 부정교합을 개선하고 안정된 결과를 얻을 수 있습니다.",
    "translated": "A. 雙顎手術是能夠解決骨骼畸形的手術方式，手術後將骨骼位置重新調整至正確位置時，牙齒的咬合關係可能會改變。因此，雙顎手術後可能需要進行牙齒矯正，透過手術與矯正的跨科協作，可改善錯咬合並獲得穩定的治療成果。",
    "location": "line:1521, tag:strong",
    "context": "text"
  },
  {
    "key": "text_90_span",
    "text": "주걱턱 교정은 누구에게 필요한가요?",
    "translated": "戽斗矯正適合哪些人？",
    "location": "line:1527, tag:span",
    "context": "text"
  },
  {
    "key": "text_91_strong",
    "text": "A. 주걱턱 교정은 아래턱 성장이 과도하거나 위턱 성장이 상대적으로 부족해서 아래턱이 튀어나온 경우에 필요합니다. 얼굴이 길어 인상이 강해보이거나 나이가 들어 보이는 경우, 위아래 치아가 거꾸로 물려 저작 효율이 떨어지는 경우에도 교정을 통해 개선할 수 있습니다.",
    "translated": "A. 戽斗矯正適用於下顎過度生長或上顎相對發育不足導致下顎突出的情況。臉型較長而顯得表情強硬或看起來較老，以及上下牙齒反咬導致咀嚼效率下降的情況，也可透過矯正加以改善。",
    "location": "line:1531, tag:strong",
    "context": "text"
  },
  {
    "key": "text_92_span",
    "text": "교정 기간은 보통 얼마나 걸리나요?",
    "translated": "矯正療程通常需要多久？",
    "location": "line:1537, tag:span",
    "context": "text"
  },
  {
    "key": "text_93_strong",
    "text": "A. 일반적으로 전체 교정은 12~24개월, 부분 교정은 3~6개월 정도 소요됩니다. 환자의 치아 상태, 교정 난이도, 사용하는 장치 종류에 따라 기간이 달라질 수 있으며, 정확한 기간은 정밀 진단 후 안내해 드립니다.",
    "translated": "A. 一般而言，全口矯正約需 12～24 個月，局部矯正約需 3～6 個月。實際療程因患者的牙齒狀況、矯正難易度及使用裝置種類而有所不同，精確的療程時間將於精密診斷後詳細說明。",
    "location": "line:1541, tag:strong",
    "context": "text"
  },
  {
    "key": "text_94_span",
    "text": "교정 후 유지장치는 꼭 해야 하나요?",
    "translated": "矯正後一定要配戴保持器嗎？",
    "location": "line:1547, tag:span",
    "context": "text"
  },
  {
    "key": "text_95_strong",
    "text": "A. 네, 교정 완료 후 유지장치 착용은 매우 중요합니다. 치아는 원래 위치로 돌아가려는 경향이 있기 때문에, 교정 결과를 안정적으로 유지하기 위해 일정 기간 유지장치를 착용해야 합니다. 스마일뷰에서는 고정식 또는 가철식 유지장치를 제공하며, 정기적인 관리를 통해 장기적으로 아름다운 미소를 유지할 수 있도록 도와드립니다.",
    "translated": "A. 是的，矯正完成後配戴保持器非常重要。由於牙齒有回到原本位置的傾向，為了穩定維持矯正成果，必須在一定期間內配戴保持器。SMILEVIEW 提供固定式或活動式保持器，透過定期追蹤管理，協助您長期維持美麗的笑容。",
    "location": "line:1551, tag:strong",
    "context": "text"
  },
  {
    "key": "attr_96_button_title",
    "text": "맨 위로",
    "translated": "回到頂部",
    "location": "line:1559, tag:button[title]",
    "context": "attr:title"
  },
  {
    "key": "text_97_p",
    "text": "투명하고 편리한 교정부터 심미 치료까지, 스마일뷰치과가 당신의 아름다운 미소를 만들어 드립니다.",
    "translated": "從透明舒適的矯正到美觀治療，SMILEVIEW牙醫診所為您打造美麗的笑容。",
    "location": "line:1572, tag:p",
    "context": "text"
  },
  {
    "key": "text_98_li",
    "text": "서울특별시 강남구 봉은사로 107, 15층",
    "translated": "首爾特別市 江南區 奉恩寺路 107, 15樓",
    "location": "line:1577, tag:li",
    "context": "text"
  },
  {
    "key": "text_99_li",
    "text": "(논현동 201 16번지 15층)",
    "translated": "（論峴洞 201 16番地 15樓）",
    "location": "line:1578, tag:li",
    "context": "text"
  },
  {
    "key": "text_100_li",
    "text": "대표자 김한결",
    "translated": "代表人 金韓結",
    "location": "line:1586, tag:li",
    "context": "text"
  },
  {
    "key": "text_101_li",
    "text": "사업자번호 699-29-00572",
    "translated": "營業登記號 699-29-00572",
    "location": "line:1587, tag:li",
    "context": "text"
  },
  {
    "key": "text_102_li",
    "text": "평일 AM 10:00 - PM 06:30",
    "translated": "平日 AM 10:00 - PM 06:30",
    "location": "line:1593, tag:li",
    "context": "text"
  },
  {
    "key": "text_103_li",
    "text": "점심시간 PM 01:00 - PM 02:00",
    "translated": "午休時間 PM 01:00 - PM 02:00",
    "location": "line:1594, tag:li",
    "context": "text"
  },
  {
    "key": "text_104_li",
    "text": "토요일 AM 10:00 - PM 03:00",
    "translated": "週六 AM 10:00 - PM 03:00",
    "location": "line:1595, tag:li",
    "context": "text"
  },
  {
    "key": "text_105_li",
    "text": "점심시간 없이 진료",
    "translated": "無午休持續看診",
    "location": "line:1596, tag:li",
    "context": "text"
  },
  {
    "key": "text_106_li",
    "text": "일요일 AM 10:00 - PM 04:00",
    "translated": "週日 AM 10:00 - PM 04:00",
    "location": "line:1597, tag:li",
    "context": "text"
  },
  {
    "key": "text_107_li",
    "text": "휴진 공휴일",
    "translated": "休診 國定假日",
    "location": "line:1598, tag:li",
    "context": "text"
  }
]

output_path = '/c/Users/rlcks/OneDrive/Desktop/SMILEVIEW/translations/tw/ortho.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'Done: {output_path}')
print(f'Total items: {len(data)}')
