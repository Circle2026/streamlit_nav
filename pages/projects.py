import streamlit as st
st.markdown(
	"""
	<style>
	.project-card {
		padding: 1.5rem;
		margin-top: 1.25rem;
		background-color: #FFFDF8;
		border: 1px solid #DDD8CC;
		border-radius: 8px;
	}
	.project-card p {
		color: #66736D;
		line-height: 1.7;
	}
	</style>
	""",
	unsafe_allow_html=True
)
st.title("作品集",icon=":material/business_center:")
#st.markdown('<div class="project-card">', unsafe_allow_html=True)
st.write("Projects page")
st.markdown('</div>', unsafe_allow_html=True)
