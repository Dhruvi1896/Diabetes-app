import streamlit as st
import numpy as np
import pickle
import os
import time
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Diabetes Predictor", page_icon="🩺")

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🩺 Diabetes Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>AI-powered health prediction system</p>", unsafe_allow_html=True)
st.markdown("---")

# Load model
model_path = "diabetes_model.pkl"
if not os.path.exists(model_path):
    st.error("⚠️ Model file not found")
    st.stop()

model = pickle.load(open(model_path, "rb"))

# Sidebar
st.sidebar.title("ℹ️ About")
st.sidebar.info("This app uses Machine Learning (SVM) to predict diabetes.")

# Input layout
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

# Predict
if st.button("🔍 Predict"):
    with st.spinner("Analyzing..."):
        time.sleep(2)

    input_data = np.array([[pregnancies, glucose, blood_pressure,
                            skin_thickness, insulin, bmi, dpf, age]])

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    st.markdown("## 🧾 Result")

    if prediction[0] == 1:
        st.error(f"⚠️ Diabetic (Confidence: {probability[0][1]*100:.2f}%)")
    else:
        st.success(f"✅ Not Diabetic (Confidence: {probability[0][0]*100:.2f}%)")

    # 📊 Comparison Chart
    st.markdown("## 📊 Your Data vs Average")

    avg_values = [3.8, 120, 69, 20, 79, 32, 0.47, 33]
    labels = ["Preg", "Glu", "BP", "Skin", "Ins", "BMI", "DPF", "Age"]

    user_values = [pregnancies, glucose, blood_pressure,
                   skin_thickness, insulin, bmi, dpf, age]

    df = pd.DataFrame({
        "Feature": labels,
        "Your Values": user_values,
        "Average": avg_values
    })

    fig, ax = plt.subplots()
    ax.plot(labels, user_values, marker='o', label="You")
    ax.plot(labels, avg_values, marker='o', label="Average")
    ax.legend()
    ax.set_title("Health Comparison")

    st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>🚀 Built with Streamlit | ML Project</p>", unsafe_allow_html=True)ue)t-align: center;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)   