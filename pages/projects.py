import streamlit as st

st.title("專案首頁")


with st.sidebar:
    st.write("專案清單")
    st.write("**專案說明")
    st.write("**專案功能")
    st.write("**專案使用工具")

    st.page_link(st.Page("pages/myproject1.py" ), label="財經分析專題",icon="🐷" )
    # st.page_link("pages/project2.py" , label="市場調查專題" )
   
    st.page_link("https://github.com/Circle2026" , label="github其他專題",icon=":material/merge:" )