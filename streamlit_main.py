import streamlit as st
pgnv=st.navigation(
    pages=[st.Page("pages/home.py",title="Home")],
    position="sidebar"
)
pgnv.run()
