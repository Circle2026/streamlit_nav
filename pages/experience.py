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
    st.markdown('<div class="right-column">我過去曾任職於食品技師，具備食品安全管理、品質管理與餐飲營運的產業專業知識，熟悉 HACCP、ISO 22000、SOP、文件管理及作業流程監控。</div>', 
                unsafe_allow_html=True)
    st.markdown('<div class="right-column">負責監督食品製備與作業流程，確保現場執行符合衛生與食品安全標準；透過日常流程監控、文件紀錄與異常處理，協助維持作業品質並降低食品安全風險。</div>', 
                unsafe_allow_html=True)
    st.markdown('<div class="right-column">此段經歷培養了流程管理、問題辨識、風險分析、標準化及跨部門協作能力，也讓我具備從實際營運流程理解問題、整理資訊並尋找改善方向的經驗，成為轉向資料分析與商業分析領域的產業基礎。</div>', 
                unsafe_allow_html=True)

st.divider()
col3, col4 = st.columns(2)
with col3:
    st.markdown('<div class="section-title">海外工作經歷</div>', unsafe_allow_html=True) 
    
    st.markdown("**愛爾蘭海外工作經驗**")
    st.markdown('<span class="subtext">2025-2026</span>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="right-column">獨立規劃並完成為期 8 個月的愛爾蘭海外工作與生活，在全英語及多元文化環境中工作，培養快速適應新環境、獨立解決問題及跨文化溝通的能力。</div>', 
                unsafe_allow_html=True)
    st.markdown('<div class="right-column">與來自不同國家的同事共同工作，學習適應不同的工作方式與溝通模式，提升團隊協作、問題解決與國際工作環境下的應變能力。</div>', 
                unsafe_allow_html=True)
