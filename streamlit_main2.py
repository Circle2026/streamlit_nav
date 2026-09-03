import streamlit as st

pageList=[
    st.Page("pages/home.py",title="Home"),
    st.Page("pages/mycv.py",title="我的履歷"),
    st.Page("pages/myproject.py",title="執行專案"),
]
pgnv=st.navigation(
    pages=pageList,
    position="top"
)
pgnv.run()