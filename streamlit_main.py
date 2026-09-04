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

    /* =====================================================
       GLOBAL
       ===================================================== */

    .stApp {
        background-color: #F7F7F5;
        color: #202124;
    }


    /* =====================================================
       MAIN CONTENT
       ===================================================== */

    .main .block-container {
        max-width: 1100px;

        padding-top: 5rem;
        padding-bottom: 6rem;

        padding-left: 4rem;
        padding-right: 4rem;
    }


    /* =====================================================
       TOP NAVIGATION
       ===================================================== */

    [data-testid="stHeader"] {
        background-color: #F7F7F5;
    }


    /* =====================================================
       TYPOGRAPHY
       ===================================================== */

    body {
        font-family:
            -apple-system,
            BlinkMacSystemFont,
            "Segoe UI",
            "Noto Sans TC",
            sans-serif;
    }


    /* =====================================================
       SIDEBAR
       ===================================================== */

    section[data-testid="stSidebar"] {

        background-color: #EFEFEA;

        border-right: 1px solid #DEDED8;
    }


    section[data-testid="stSidebar"] .block-container {

        padding-top: 3rem;
        padding-left: 1.5rem;
        padding-right: 1.5rem;
    }


    /* =====================================================
       SIDEBAR BUTTON
       ===================================================== */

    .stDownloadButton button {

        width: 100%;

        background-color: #202124;
        color: #FFFFFF;

        border: none;

        border-radius: 4px;

        padding: 0.65rem 1rem;

        font-weight: 500;
    }


    .stDownloadButton button:hover {

        background-color: #3C4043;

        color: #FFFFFF;
    }


    /* =====================================================
       DIVIDER
       ===================================================== */

    hr {

        border: none;

        border-top: 1px solid #DADAD4;

        margin-top: 2.5rem;
        margin-bottom: 2.5rem;
    }


    /* =====================================================
       REMOVE EXTRA STREAMLIT SPACING
       ===================================================== */

    .element-container {

        margin-bottom: 0.25rem;
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
    position="top"
)

pg.run()
