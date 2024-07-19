import streamlit as st
import numpy as np
from PIL import Image
from utils import predict

st.set_page_config(
    page_title="Pneumonia Classification ", 
    page_icon="🩺",
    layout="wide"
)

st.markdown("""
    <style>
    .title-center {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        color: #3498db;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="title-center">🩺 Pneumonia Classification 🩺</h1>', unsafe_allow_html=True)

# st.title('Pneumonia classification')

# set header
st.subheader('Please upload a chest X-ray image',divider="rainbow")

# upload file
uploded_file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])
st.button('Submit')

if uploded_file is not None:
    image = Image.open(uploded_file).convert('RGB')

    # classify image
    prediction = predict(np.array(image))

    if prediction==0:
        col1,col2,col3=st.columns(3)
        with col1:
            st.image(image,use_column_width="auto",width=300)
        with col2:
            st.success("with Go blessings you're safe!", icon="✅")
        with col3:
            st.image("assets\safe.jpg",width=300)
    if prediction==1:
        col1,col2,col3=st.columns(3)
        with col1:
            st.image(image,use_column_width="auto",width=300)
        with col2:
            st.error("There is penumonia detected! Consult a Doctor", icon="🚨")
        with col3:
            st.image("assets\danger.jpg",width=300)

with st.sidebar:
        st.markdown("""
        <div style="padding: 10px; border: 2px solid #ffffff; border-radius: 5px; background-color: #0E1117; color: #ffffff; width: fit-content;">
        <b>⚠️Disclaimer⚠️</b>:<br></br>This tool is not intended for self-diagnosis. Always consult a doctor for medical advice.
        </div>
        """, unsafe_allow_html=True)
