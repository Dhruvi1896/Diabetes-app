import streamlit as st
import numpy as np
import pickle
import os
import time

# Page config
st.set_page_config(page_title="Diabetes Predictor", page_icon="🩺", layout="centered")

# Custom CSS (frontend feel)
st.markdown("""
<style>
body {
    background-color: #f5f7fa;
}
.main {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🩺 Diabetes Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter patient details to predict diabetes</p>", unsafe_allow_html=True)
st.markdown("---")

# Load model
model_path = "diabetes_model.pkl"
if not os.path.exists(model_path):
    st.error("⚠️ Model file not found")
    st.stop()

model = pickle.load(open(model_path, "rb"))

# Sidebar
st.sidebar.title("ℹ️ About")
st.sidebar.info("This app predicts whether a person is diabetic using a Machine Learning model (SVM).")

# Input layout (2 columns)
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Pregnancies", min_value=0)
    glucose = st.number_input("Glucose", min_value=0)
    blood_pressure = st.number_input("Blood Pressure", min_value=0)
    skin_thickness = st.number_input("Skin Thickness", min_value=0)

with col2:
    insulin = st.number_input("Insulin", min_value=0)
    bmi = st.slider("BMI", 10.0, 50.0, 25.0)
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
    age = st.slider("Age", 1, 100, 25)

st.markdown("---")

# Predict button
if st.button("🔍 Predict"):
    with st.spinner("Analyzing data..."):
        time.sleep(2)

    input_data = np.array([[pregnancies, glucose, blood_pressure,
                            skin_thickness, insulin, bmi, dpf, age]])

    prediction = model.predict(input_data)

    st.markdown("### 🧾 Result")

    if prediction[0] == 1:
        st.error("⚠️ The person is **Diabetic**")
    else:
        st.success("✅ The person is **Not Diabetic**")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)'text-align: center;'>🚀 Built with Streamlit | ML Project</p>", unsafe_allow_html=True)ue)t-align: center;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)   