import streamlit as st
import numpy as np
import pickle
import os
st.title("Diabetes Prediction App")
model_path = ("diabetes_model.pkl")
if not os.path.exists(model_path):
    st.error("Model file not found")
    st.stop()
model = pickle.load(open(model_path,"rb"))
st.write("enter patient details")
pregnancies = st.number_input("pregnanciues")
glucose = st.number_input("Glucose")
blood_pressure = st.number_input("Blood Pressure")
skin_thickness = st.number_input("Skin Thickness")
insulin = st.number_input("Insulin")
bmi = st.number_input("BMI")
dpf = st.number_input("Diabetes Pedigree Function")
age = st.number_input("Age")
if st.button("Predict"):
    input_data = np.array([[pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,dpf,age]])
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("diabetic")
    else:
        st.success("not diabetic")
    