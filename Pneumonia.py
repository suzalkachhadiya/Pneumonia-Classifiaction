import streamlit as st

st.set_page_config(
    page_title="Pneumonia Detection", 
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

st.markdown('<h1 class="title-center">🩺 Pneumonia Detection 🩺</h1>', unsafe_allow_html=True)

st.write("\n")

st.header("● What is 'Pneumonia'?",divider="rainbow")

st.write("""Pneumonia is an inflammatory condition of the lung affecting primarily the small air sacs known as alveoli.Symptoms typically include some combination of productive or dry cough, chest pain, fever and difficulty breathing.
          The severity of the condition is variable.""")
col1, col2, col3 = st.columns(3)
with col2:
    st.image("assets/neumonia_decease.jpg",width=300)
st.write("""Pneumonia is usually caused by infection with viruses or bacteria and less commonly by other microorganisms, certain medications or conditions such as autoimmune diseases.
         Risk factors include cystic fibrosis, chronic obstructive pulmonary disease (COPD), asthma, diabetes, heart failure, a history of smoking, a poor ability to cough such as following a stroke and a weak immune system. 
         Diagnosis is often based on symptoms and physical examination. Chest X-ray, blood tests, and culture of the sputum may help confirm the diagnosis.The disease may be classified by where it was acquired, such as community- or hospital-acquired or healthcare-associated pneumonia.
         """)

st.header("How it works?", divider="rainbow")
st.write("""Leveraging cutting-edge AI, this tool analyzes chest X-rays with high accuracy, assisting healthcare professionals in pneumonia detection. Upload your X-ray to get started.""")

st.header("What is the approach behind it?", divider="rainbow")
st.write("""This tool utilizes a Convolutional Neural Network (CNN), a powerful type of AI model, to analyze chest X-ray images and identify patterns that may indicate pneumonia.""")

with st.sidebar:
        st.markdown("""
        <div style="padding: 10px; border: 2px solid #ffffff; border-radius: 5px; background-color: #0E1117; color: #ffffff; width: fit-content;justify-content: center;">
        ⚠️<b>Disclaimer:</b><br></br>This tool is not intended for self-diagnosis.<br></br>Always consult a doctor for medical advice.
        </div>
        """, unsafe_allow_html=True)
