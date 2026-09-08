import streamlit as st
st.markdown(
    """
    <style>
    .home-hero {
        padding: 2.5rem 0 2rem;
        border-bottom: 1px solid #DDD8CC;
        margin-bottom: 2.5rem;
    }

    .home-hero h1 {
        margin-bottom: 0.35rem;
        color: #1F2933;
        font-size: clamp(2.5rem, 7vw, 4.75rem);
        letter-spacing: 0.02em;
    }
    .home-hero h2 {
        color: #2F6B57;
        font-size: clamp(1.2rem, 2.5vw, 1.75rem);
        margin-bottom: 0.65rem;
    }
    .home-introduction {
        max-width: 720px;
        margin: 0 auto 3rem;
        padding: 1.25rem 1.5rem;
        border-left: 3px solid #C98B5B;
        background-color: #FFFDF8;
        text-align: left;
    }
    .home-skills {
        padding: 1.25rem 1.5rem;
        background-color: #FFFDF8;
        border: 1px solid #DDD8CC;
        border-radius: 8px;
        text-align: center;
    }
    .home-skills strong {
        color: #1F2933;
    }
    section[data-testid="stSidebar"] [data-testid="stDownloadButton"] button {
        background-color: #2F6B57 !important;
        border: 1px solid #2F6B57 !important;
        color: #FFFDF8 !important;
        font-weight: 700 !important;
    }
    section[data-testid="stSidebar"] [data-testid="stDownloadButton"] button p,
    section[data-testid="stSidebar"] [data-testid="stDownloadButton"] button span {
        color: #FFFDF8 !important;
    }
    section[data-testid="stSidebar"] [data-testid="stDownloadButton"] button:hover {
        background-color: #245844 !important;
        border-color: #245844 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# ==================================================
# Hero
# ==================================================
st.markdown('<div class="home-hero">', unsafe_allow_html=True)
st.markdown("# YUANSIN", text_alignment="center")
st.markdown("## :blue[Data Analyst / BI Analyst]", text_alignment="center")
st.markdown(
    "Food Technologist  →  Data & Business Intelligence",
    text_alignment="center"
)
st.markdown("</div>", unsafe_allow_html=True)
# ==================================================
# Introduction
# ==================================================
st.markdown('<div class="home-introduction">', unsafe_allow_html=True)
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
st.markdown("</div>", unsafe_allow_html=True)
# ==================================================
# Core Skills
# ==================================================
st.markdown('<div class="home-skills">', unsafe_allow_html=True)
st.markdown(":small[CORE SKILLS]", text_alignment="center")
st.markdown(
    """
    **SQL Server**  ·  **Python**  ·  **Power BI**
    **SSAS**  ·  **SSRS**
    """,
    text_alignment="center"
)
st.markdown("</div>", unsafe_allow_html=True)
# ==================================================
# Sidebar — Resume
# ==================================================
st.sidebar.title("Resume")
st.sidebar.write(
    "Want to know more about me?"
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
st.sidebar.caption("yuansinwan@gmail.com")
st.sidebar.markdown("**LinkedIn**")
st.sidebar.caption("linkedin.com/in/your-profile")
st.sidebar.markdown("**GitHub**")
st.sidebar.caption("https://github.com/Circle2026")
