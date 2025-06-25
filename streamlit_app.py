# app/streamlit_app.py

import streamlit as st
import numpy as np
import joblib

# Title & description
st.set_page_config(page_title="COVID-19 Unemployment Predictor", layout="centered")
st.title("🦠 COVID-19 Economic Impact – India")
st.subheader("📈 Predict Unemployment Rate from COVID-19 Stats")

# Load trained model
model = joblib.load("src/unemployment_model.pkl")

# User inputs
st.markdown("### 🔢 Enter COVID-19 Statistics:")
confirmed = st.number_input("Confirmed Cases", min_value=0, step=1)
deaths = st.number_input("Deaths", min_value=0, step=1)
recovered = st.number_input("Recovered", min_value=0, step=1)

# Compute active cases automatically
active = confirmed - deaths - recovered
if active < 0:
    active = 0

st.markdown(f"🧮 **Active Cases (Auto-Calculated):** `{active}`")

# Predict button
if st.button("🎯 Predict Unemployment Rate"):
    input_data = np.array([[confirmed, deaths, recovered, active]])
    prediction = model.predict(input_data)[0]
    st.success(f"📊 Predicted Unemployment Rate: **{prediction:.2f}%**")
