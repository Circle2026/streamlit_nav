import streamlit as st


# ==================================================
# Page Title
# ==================================================

st.title("Skills")

st.caption(
    "技術能力與專業領域，持續累積資料分析、商業智慧與資料工程相關實務能力。"
)


# ==================================================
# 資料與商業智慧
# ==================================================

st.header("資料與商業智慧")

data_skills = [
    ("SQL Server", "資料庫查詢、資料處理與 SQL 資料分析。"),
    ("Power BI", "資料視覺化、互動式 Dashboard 與商業報表開發。"),
    ("SSAS", "資料模型建立、語意模型與分析解決方案。"),
    ("SSRS", "報表開發、資料呈現與商業報表製作。"),
]

data_columns = st.columns(2)
for index, (skill_name, description) in enumerate(data_skills):
    with data_columns[index % 2]:
        with st.container(border=True):
            st.markdown(f"**{skill_name}**")
            st.write(description)


# ==================================================
# 程式設計
# ==================================================

st.header("程式設計")

with st.container(border=True):
    st.markdown("**Python**")
    st.write("資料分析、資料處理、自動化與網路資料擷取。")


# ==================================================
# 開發與版本控制
# ==================================================

st.header("開發與版本控制")

development_skills = [
    ("Git", "版本控制與程式碼管理。"),
    ("GitHub", "專案版本管理、文件維護與作品展示。"),
    ("VS Code", "Python 開發與資料處理環境。"),
    ("Visual Studio", "Microsoft BI 相關開發環境。"),
]

development_columns = st.columns(2)
for index, (skill_name, description) in enumerate(development_skills):
    with development_columns[index % 2]:
        with st.container(border=True):
            st.markdown(f"**{skill_name}**")
            st.write(description)


# ==================================================
# 資料應用開發
# ==================================================

st.header("資料應用開發")

with st.container(border=True):
    st.markdown("**Streamlit**")
    st.write("使用 Python 建立互動式資料應用程式與 Web Application。")


# ==================================================
# 領域知識
# ==================================================

st.header("領域知識")

domain_skills = [
    ("食品安全管理", "HACCP · ISO 22000 · Food Safety"),
    ("文件與流程管理", "文件控管 · 流程管理 · 品質管理"),
]

domain_columns = st.columns(2)
for index, (skill_name, description) in enumerate(domain_skills):
    with domain_columns[index]:
        with st.container(border=True):
            st.markdown(f"**{skill_name}**")
            st.write(description)

# ==================================================
# 目前學習中
# ==================================================

st.header("目前學習中")

st.caption("持續拓展雲端資料平台與資料取得相關能力。")

learning_skills = [
    ("Snowflake", "學習雲端資料倉儲架構與 Snowflake 平台應用。"),
    ("Web Scraping", "使用 Python 進行網路資料擷取、清理與整理。"),
    ("SSIS", "ETL、資料整合與資料轉換。")
]

learning_columns = st.columns(2)
for index, (skill_name, description) in enumerate(learning_skills):
    with learning_columns[index % 2]:
        with st.container(border=True):
            st.markdown(f"**{skill_name}**")
            st.write(description)


# ==================================================
# 證照與語言能力
# ==================================================

st.header("證照與語言能力")

certification_skills = [
    ("Google Analytics Certification", "Google Analytics 4"),
    ("TOEIC", "Score XXX"),
    ("食品安全相關證照", "HACCP A/B"),
    ("食品技師", "食品技師"),
]

certification_columns = st.columns(2)
for index, (skill_name, description) in enumerate(certification_skills):
    with certification_columns[index % 2]:
        with st.container(border=True):
            st.markdown(f"**{skill_name}**")
            st.write(description)


