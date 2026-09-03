import streamlit as st

pages = [
    st.Page("pages/home.py", title="Home", icon=":material/home:"),
    st.Page("pages/experience.py", title="Experience", icon=":material/assignment_globe:"),
    st.Page("pages/skills.py", title="Skills", icon=":material/cognition:"),
    st.Page("pages/projects.py", title="Projects", icon=":material/pinboard:"),
]

pg = st.navigation(
    pages,
    position="top"
)

pg.run()

