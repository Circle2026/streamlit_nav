import streamlit as st

st.set_page_config(
    page_title="YUANSIN | Data Analyst",
    page_icon="🏠",
    layout="wide"
)

# =========================
# CSS
# =========================

st.markdown("""
<style>

.main {
    background-color: #F8FAFC;
}

/* 主標題 */
.big-title {
    font-size: 56px;
    font-weight: 800;
    color: #0F172A;
}

/* 副標題 */
.job-title {
    font-size: 28px;
    font-weight: 600;
    color: #2563EB;
}

/* 一般文字 */
.description {
    font-size: 18px;
    line-height: 1.8;
    color: #475569;
}

/* 重點文字 */
.highlight {
    color: #2563EB;
    font-weight: 700;
}

/* Career box */
.career-box {
    background-color: #EFF6FF;
    border-left: 5px solid #2563EB;
    padding: 20px;
    border-radius: 10px;
    margin: 25px 0;
}

.career-text {
    font-size: 24px;
    font-weight: 700;
    color: #1E3A8A;
}

/* Section */
.section-title {
    font-size: 28px;
    font-weight: 700;
    color: #0F172A;
    margin-top: 30px;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)


# =========================
# Hero
# =========================

st.markdown(
    '<div class="big-title">YUANSIN</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="job-title">Data Analyst / BI Analyst</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="description">Career Changer · Data & Business Intelligence</div>',
    unsafe_allow_html=True
)


# =========================
# Career Transition
# =========================

st.markdown(
    """
    <div class="career-box">
        <div class="career-text">
            Food Technologist → Data & Business Intelligence
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================
# About Me
# =========================

st.markdown(
    '<div class="section-title">About Me</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="description">
        我過去曾任職於
        <span class="highlight">食品技師</span>，
        主要累積食品安全管理、HACCP、ISO 22000、
        文件管理與流程管理等相關經驗。
    </div>
    """,
    unsafe_allow_html=True
)


# =========================
# Current Direction
# =========================

st.markdown(
    '<div class="section-title">Current Direction</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="description">
        目前正轉職往
        <span class="highlight">資料分析師（Data Analyst）</span>
        ／
        <span class="highlight">商業智慧分析師（BI Analyst）</span>
        發展。
        <br><br>
        持續建立 SQL Server、Python、Power BI、
        SSAS、SSRS 等資料分析與 BI 技能。
    </div>
    """,
    unsafe_allow_html=True
)


# =========================
# Technical Skills
# =========================

st.markdown(
    '<div class="section-title">Technical Skills</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4, col5 = st.columns(5)

col1.info("SQL Server")
col2.info("Python")
col3.info("Power BI")
col4.info("SSAS")
col5.info("SSRS")


# =========================
# Sidebar
# =========================

st.sidebar.title("📄 Resume")

st.sidebar.write(
    "Want to know more about my experience?"
)

st.sidebar.download_button(
    label="Download Resume PDF",
    data=b"Dummy resume content for testing",
    file_name="resume.pdf",
    mime="application/pdf",
    icon="📥"
)
