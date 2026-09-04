import streamlit as st


# ==================================================
# Hero
# ==================================================

st.markdown(
    "# YUANSIN",
    text_alignment="center"
)

st.markdown(
    "## :blue[Data Analyst / BI Analyst]",
    text_alignment="center"
)

st.markdown(
    "Food Technologist  →  Data & Business Intelligence",
    text_alignment="center"
)


st.write("")
st.write("")


# ==================================================
# Introduction
# ==================================================

st.markdown(
    """
    我過去曾任職於食品產業，累積食品安全管理、
    HACCP、ISO 22000、文件管理與流程管理等相關經驗。

    目前專注於 :green[Data Analysis] 與
    :green[Business Intelligence]，
    持續建立資料庫、程式與 BI 分析能力。
    """,
    text_alignment="center"
)


st.write("")
st.write("")
st.write("")


# ==================================================
# Core Skills
# ==================================================

st.markdown(
    ":small[CORE SKILLS]",
    text_alignment="center"
)

st.write("")

st.markdown(
    """
    **SQL Server**  ·  **Python**  ·  **Power BI**

    **SSAS**  ·  **SSRS**
    """,
    text_alignment="center"
)


# ==================================================
# Sidebar — Resume
# ==================================================

st.sidebar.title("Resume")

st.sidebar.write(
    "Want to know more about my experience?"
)

st.sidebar.download_button(
    label="Download Resume PDF",
    data=b"Dummy resume content for testing",
    file_name="resume.pdf",
    mime="application/pdf",
    icon=":material/download:"
)


# ==================================================
# Sidebar — Contact
# ==================================================

st.sidebar.divider()

st.sidebar.title("Contact")


st.sidebar.markdown("**Email**")
st.sidebar.caption("your-email@example.com")


st.sidebar.markdown("**LinkedIn**")
st.sidebar.caption("linkedin.com/in/your-profile")


st.sidebar.markdown("**GitHub**")
st.sidebar.caption("github.com/Circle2026")
