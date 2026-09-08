import streamlit as st


# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="YUANSIN | Data Analyst / BI Analyst",
    page_icon=":material/analytics:",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# Global CSS
# =========================================================

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Noto+Sans+TC:wght@400;500;600;700&display=swap');

    .stApp {
        background-color: #F5F3EE;
        color: #1F2933;
    }

    .main .block-container {
        max-width: 1180px;
        padding-top: 3.75rem;
        padding-bottom: 5rem;
        padding-left: clamp(1.25rem, 4vw, 4rem);
        padding-right: clamp(1.25rem, 4vw, 4rem);
    }

    [data-testid="stHeader"] {
        background-color: #F5F3EE;
    }

    body {
        font-family: "Inter", "Noto Sans TC", sans-serif;
    }

    h1, h2, h3, h4, p, li, button, label {
        font-family: "Inter", "Noto Sans TC", sans-serif;
    }

    h1 {
        color: #1F2933;
        font-weight: 700;
        letter-spacing: 0;
    }

    h2, h3 {
        color: #1F2933;
        font-weight: 600;
        letter-spacing: 0;
    }

    p, li {
        color: #66736D;
        line-height: 1.75;
    }

    a {
        color: #2F6B57;
    }

    [data-testid="stCaptionContainer"] p {
        color: #66736D;
    }

    section[data-testid="stSidebar"] {
        background-color: #FFFDF8;
        border-right: 1px solid #DDD8CC;
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 2rem;
        padding-left: 1.25rem;
        padding-right: 1.25rem;
    }

    .stDownloadButton button {
        width: 100%;
        background-color: #2F6B57;
        color: #FFFDF8;
        border: 1px solid #2F6B57;
        border-radius: 6px;
        padding: 0.65rem 1rem;
        font-weight: 600;
    }

    .stDownloadButton button:hover {
        background-color: #245844;
        border-color: #245844;
        color: #FFFDF8;
    }

    hr {
        border: none;
        border-top: 1px solid #DDD8CC;
        margin-top: 2rem;
        margin-bottom: 2rem;
    }

    .element-container {
        margin-bottom: 0.45rem;
    }

    [data-testid="stSidebarNav"] {
        border-bottom: 1px solid #DDD8CC;
        padding-bottom: 1rem;
        margin-bottom: 1.5rem;
    }

    [data-testid="stSidebarNavLink"] {
        border-radius: 6px;
        color: #66736D;
        font-weight: 500;
    }

    [data-testid="stSidebarNavLink"]:hover {
        background-color: #F3ECE3;
        color: #2F6B57;
    }

    [data-testid="stSidebarNavLink"].st-emotion-cache-1c7y2kd,
    [data-testid="stSidebarNavLink"]:has([aria-current="page"]) {
        background-color: #F3ECE3;
        color: #2F6B57;
    }

    @media (max-width: 640px) {
        .main .block-container {
            padding-top: 2.25rem;
            padding-bottom: 3rem;
        }

        h1 {
            font-size: 2.25rem;
        }

        h2 {
            font-size: 1.55rem;
        }
    }


    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# Navigation
# =========================================================

pages = [

    st.Page(
        "pages/home.py",
        title="Home",
        icon=":material/home:"
    ),

    st.Page(
        "pages/experience.py",
        title="Experience",
        icon=":material/work:"
    ),

    st.Page(
        "pages/skills.py",
        title="Skills",
        icon=":material/psychology:"
    ),

    st.Page(
        "pages/projects.py",
        title="Projects",
        icon=":material/bar_chart:"
    ),
]


pg = st.navigation(
    pages,
    position="sidebar"
)

pg.run()
