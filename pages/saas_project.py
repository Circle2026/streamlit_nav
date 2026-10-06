import re
from pathlib import Path

import streamlit as st


IMAGE_DIRECTORY = Path(__file__).resolve().parents[1] / "images" / "contoso"
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}

IMAGE_NOTES = [
	(
		"01｜績效總覽",
		"客戶流失比例為何?是否隨時間有客戶流失趨勢?",
	),
	(
		"02｜分析範圍與指標",
		"確認資料期間、指標定義與篩選條件，讓後續頁面的比較維持一致口徑。",
	),
	(
		"03｜促銷活動概況",
		"由活動整體表現切入，檢視促銷情境下的銷售與獲利指標如何呈現。",
	),
	(
		"04｜折扣與營收觀察",
		"將折扣條件與營收表現並列，作為評估促銷是否帶動消費的觀察起點。",
	),
	(
		"05｜折扣與淨利分析",
		"把營收與淨利一併檢視，避免只以銷售成長判斷促銷成效。",
	),
	(
		"06｜商品表現比較",
		"比較不同商品的促銷表現，辨識適合進一步檢視的品類差異。",
	),
	(
		"07｜市場差異觀察",
		"從市場或地區維度切分表現，觀察促銷效果是否因客群與銷售環境而異。",
	),
	(
		"08｜顧客消費行為",
		"將顧客消費相關指標納入閱讀脈絡，理解促銷與購買行為之間的可能關係。",
	),
	(
		"09｜訂單趨勢檢視",
		"沿時間與訂單表現檢視變化，為比較不同促銷期間提供脈絡。",
	),
	(
		"10｜產品類別與客群交叉觀察",
		"交叉檢視商品與顧客面向，尋找值得再深入分析的消費差異。",
	),
	(
		"11｜獲利貢獻檢視",
		"回到淨利與獲利貢獻，評估促銷帶來的營收變化是否伴隨獲利改善。"
	),
	(
		"12｜互動分析與明細",
		"透過報表中的互動與篩選逐步縮小分析範圍，追查彙總指標背後的細節。",
	),
	(
		"13｜分析回顧",
		"整合前述觀察，將促銷、淨利與顧客消費行為放在同一決策脈絡中檢視。",
	),
]


def natural_sort_key(path: Path) -> tuple[str | int, ...]:
	return tuple(
		int(part) if part.isdigit() else part.casefold()
		for part in re.split(r"(\d+)", path.name)
	)


st.title("客戶流失情形與客服滿意度分析\nSAAS Customer Churn Analysis", icon=":material/analytics:")
st.markdown("Looker Studio 商業分析儀表板｜客戶流失、不同國家/產業別/訂閱產品類型以及顧客滿意度")

st.divider()
st.header("專案背景")
st.markdown(
	"本專案聚焦折扣促銷與企業營運表現之間的關係。透過整理銷售、折扣、淨利與顧客消費相關資訊，"
	"建立互動式 Power BI 儀表板，讓使用者能從整體指標逐步探索不同面向，並以資料支持促銷策略評估。"
)

st.divider()
st.header("分析目標（Business Questions）")
st.markdown(
	"- 客戶流失？\n"
	"- 不同國家/產業別/訂閱產品類型\n"
	"- 客服滿意度、客服處理速度" \
)

st.divider()
st.header("技術工具")
tool_columns = st.columns(4)
for column, tool_name, detail in zip(
	tool_columns,
	("Looker Studio", "SQL", "Data Modeling","Python清洗資料"),
	(
		"互動式儀表板與資料視覺化",
		"資料查詢與整理",
		"資料表關聯與分析模型",
		"Python資料清洗與處理"
	),
):
	with column:
		st.subheader(tool_name)
		st.caption(detail)

st.divider()
st.header("Dashboard 展示")
st.markdown("以下依圖片檔名中的頁碼排序，逐頁呈現儀表板與閱讀重點。")

image_paths = sorted(
	(
		path
		for path in IMAGE_DIRECTORY.iterdir()
		if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
	),
	key=natural_sort_key,
)

if not image_paths:
	st.info("目前找不到可展示的 Dashboard 圖片。")
else:
	for index, image_path in enumerate(image_paths):
		if index < len(IMAGE_NOTES):
			title, analysis = IMAGE_NOTES[index]
		else:
			title = image_path.stem.replace("_", " ")
			analysis = "本頁補充呈現專案儀表板內容，可搭配上方分析目標檢視相關指標。"
		st.subheader(title)
		st.markdown(analysis)
		st.image(str(image_path), use_container_width=True)
		if index < len(image_paths) - 1:
			st.divider()