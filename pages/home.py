import streamlit as st

st.title("Home",icon=":material/home_and_garden:")
st.write("""Hello,
here is who I am AND what I do.
Click the top bar to know more about me!""")
st.write("=========================================================================")
st.markdown(
    """# YUANSIN
## Data Analyst / BI Analyst
    
## Career Changer

## Food Technologist → Data & Business Intelligence

### SQL ｜ Server  ｜  Python  ｜  Power BI  ｜  SSAS  ｜  SSRS

    """,
    unsafe_allow_html=True
)

st.sidebar.title("Resume",icon="📄")

st.sidebar.write("Want to know more about my experience?") 

#with open("resume.pdf", "rb") as file: 之後有正式檔案再加上去
st.sidebar.download_button(
        label="Download Resume PDF",
        data=b"Dummy resume content for testing",#先暫時用測試的 之後再放正式檔案
        file_name="resume.pdf",
        mime="application/pdf",
        icon="📥"
    )

