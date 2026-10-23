import streamlit as st
from ga_tracking import load_ga

load_ga()

st.title("作品集", icon=":material/business_center:")
st.markdown("精選資料分析與商業智慧專案。")

# 專案 1：Contoso Promotion Analysis
with st.container(border=True):
    st.subheader("消費行為與促銷策略分析 / Contoso Promotion Analysis")
    st.markdown(
        "分析折扣促銷對企業淨利與顧客消費行為之影響，使用 Power BI 建立互動式商業分析儀表板。"
    )

    if st.button(
        "查看完整專案",
        icon=":material/open_in_new:",
        key="contoso_project"
    ):
        st.switch_page("pages/contoso_project.py")


# 專案 2：SAAS Customer Churn Analysis
with st.container(border=True):
    st.subheader("SAAS客戶流失與留存分析 / SAAS Customer Churn Analysis")
    st.markdown(
        "分析客戶流失原因與客服滿意度、產品使用行為關係，使用 Looker Studio 建立互動式商業分析儀表板。"
    )

    if st.button(
        "查看完整專案",
        icon=":material/open_in_new:",
        key="saas_project"
    ):
        st.switch_page("pages/saas_project.py")

