import streamlit as st
from PIL import Image
import base64

st.set_page_config(
    page_title="Marketeam",
    page_icon="📣",
    layout="wide"
)

# Background gradient
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #f9cb28, #9b5de5, #5f0a87);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .title-text {
        font-size: 48px;
        font-weight: 800;
        color: white;
    }

    .subtitle-text {
        font-size: 24px;
        font-weight: 300;
        color: #eee;
    }

    .btn-start {
        background-color: black;
        color: white;
        padding: 10px 30px;
        border-radius: 10px;
        font-size: 18px;
        text-decoration: none;
    }

    </style>
""", unsafe_allow_html=True)

# Layout
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<div class="title-text">Unlock Top Marketing Talent<br>You Thought Was Out of Reach –</div>', unsafe_allow_html=True)
    st.markdown('<div class="title-text" style="color:#e0e0ff;">Now Just One Click Away!</div>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<a href="#" class="btn-start">Start Project</a>', unsafe_allow_html=True)

with col2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Orbit_3.svg/1024px-Orbit_3.svg.png", caption="20k+ Specialists", use_column_width=True)

# Footer logos
st.markdown("---")
footer_cols = st.columns(5)
logos = {
    "Dreamure": "https://dummyimage.com/80x40/ffffff/000000&text=Dreamure",
    "SWITCH.WIN": "https://dummyimage.com/80x40/ffffff/000000&text=SWITCH",
    "Sphere": "https://dummyimage.com/80x40/ffffff/000000&text=Sphere",
    "PinSpace": "https://dummyimage.com/80x40/ffffff/000000&text=Pin",
    "Visionix": "https://dummyimage.com/80x40/ffffff/000000&text=Visionix"
}

for i, (name, url) in enumerate(logos.items()):
    with footer_cols[i]:
        st.image(url, width=80, caption=name)

