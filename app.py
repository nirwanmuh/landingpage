import streamlit as st
from PIL import Image

st.set_page_config(layout="wide", page_title="My Amazing App")

# Background image style
page_bg_img =
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("https://raw.githubusercontent.com/USERNAME/REPO/main/images/background.jpg");
    background-size: cover;
    background-position: center;
}}

h1, h2, h3, p {{
    color: white;
}}

.stButton>button {{
    color: white;
    background-color: #ff4b4b;
    padding: 10px;
    border-radius: 8px;
    font-size: 16px;
    border: none;
    transition: 0.3s;
}}

.stButton>button:hover {{
    background-color: #ff1e1e;
}}

footer {{
    text-align: center;
    padding: 20px;
    color: white;
    font-size: 14px;
}}
</style>


st.markdown(page_bg_img, unsafe_allow_html=True)

# Content
st.markdown("<h1 style='text-align: center;'>Selamat Datang di Aplikasi Kami</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Solusi Digital Masa Kini</h3>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.button("💡 Mulai Sekarang", use_container_width=True)

st.markdown("<br><br><hr><br>", unsafe_allow_html=True)

st.markdown("### Tentang Kami")
st.write("""
Kami adalah tim pengembang yang menyediakan solusi digital modern berbasis data dan AI. 
Dengan keahlian di bidang pemrograman, analitik data, dan machine learning, kami membantu organisasi bertransformasi secara digital.
""")

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<footer>
📧 Email: contact@example.com | 📞 Telp: +62-812-3456-7890
</footer>
""", unsafe_allow_html=True)
