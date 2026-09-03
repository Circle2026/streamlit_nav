import streamlit as st

st.title("工作經歷",icon=":material/business_center:")
#st.write("### Experience page")

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
font-size: 16px;
line-height: 1.5;
}
/*內文中的次要說明文字(年份)*/
.subtext {
    color: #555555;
    font-size: 16px;
}
</style>
""",
unsafe_allow_html=True
)

st.divider()
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="section-title">專業經歷</div>', unsafe_allow_html=True) 
    
    st.markdown("**食品技師/Food Technologist**")
    st.markdown('<span class="subtext">五星級飯店 2022-2025</span>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="right-column">我過去曾任職於食品技師，主要累積食品安全管理、HACCP、ISO 22000、文件管理與流程管理等相關經驗。</div>', 
                unsafe_allow_html=True)
    st.markdown('<div class="right-column">在五星級飯店的工作中，我負責監督食品製備過程，確保符合衛生標準，並協助制定和實施食品安全政策。</div>', 
                unsafe_allow_html=True)

st.divider()
col3, col4 = st.columns(2)
with col3:
    st.markdown('<div class="section-title">海外工作經歷</div>', unsafe_allow_html=True) 
    
    st.markdown("**愛爾蘭海外工作體驗**")
    st.markdown('<span class="subtext">2025-2026</span>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="right-column">獨自籌備並完成為期8個月的愛爾蘭海外工作與生活歷練。在全外語和不同文化背景下工作，增強了我的跨文化溝通能力和適應能力。</div>', 
                unsafe_allow_html=True)
    st.markdown('<div class="right-column">在這段期間，我學會了如何快速融入新的工作環境，並與來自世界各地的同事合作完成任務。</div>', 
                unsafe_allow_html=True)
