import streamlit as st

st.title("工作技能",icon=":material/business_center:")


st.markdown(
    """
<style>
/*左側標題樣式:加深顏色、加大字體突出*/
.section-title {
    color: #3495eb;
    font-size: 28px;
    font-weight: bold;
    letter-spacing: 1px;
}
/*右側內文樣式:往下移 調整為較柔和顏色*/
.right-column {
margin-left: 24px;
color: #555555;
font-size: 20px;
line-height: 1.5;
}
/*內文中的次要說明文字(年份)*/
.subtext {
    color: #555555;
    font-size: 20px;
}
</style>
""",
unsafe_allow_html=True
)

st.markdown('<div class="section-title">專業技能</div>', unsafe_allow_html=True)
st.markdown(":material/database:**DATABASE**")
st.markdown("""
SQL Server
SQL                  
View                 
CTE                  
Stored Procedure     
Backup / Restore""")
        
st.markdown(":material/code:**PROGRAMMING**")
st.markdown("""
Python               
Pandas                
CSV / Excel
""")

st.markdown(":material/bar_chart:**BI**")
st.markdown("""
Power BI             
Power Query          
Data Model          
DAX          
""")

st.markdown('<div class="section-title">證照</div>', unsafe_allow_html=True)

st.markdown("**Google Analytics 4 certification**")
st.markdown("** 食品技師**")
st.markdown("** Haccp A、B**")
st.markdown("** TOEIC**")


