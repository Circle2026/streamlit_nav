import streamlit as st

st.title("作品集", icon=":material/business_center:")
st.markdown("精選資料分析與商業智慧專案。")

with st.container(border=True):
	st.subheader("Contoso Promotion Analysis")
	st.markdown(
		"分析折扣促銷對企業淨利與顧客消費行為之影響，使用 Power BI 建立互動式商業分析儀表板。"
	)
	if st.button("查看完整專案", icon=":material/open_in_new:"):
		st.switch_page("pages/contoso_project.py")
