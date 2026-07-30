import streamlit as st
import joblib

# Load trained model
model = joblib.load("crop_model.pkl")

st.title("🌱 Crop Recommendation System")

st.write("Enter Soil and Weather Details")

N = st.number_input("Nitrogen")
P = st.number_input("Phosphorus")
K = st.number_input("Potassium")
temperature = st.number_input("Temperature")
humidity = st.number_input("Humidity")
ph = st.number_input("Soil pH")
rainfall = st.number_input("Rainfall")

if st.button("Recommend Crop"):

    sample = [[
        N,
        P,
        K,
        temperature,
        humidity,
        ph,
        rainfall
    ]]

    crop = model.predict(sample)

    st.success("Recommended Crop : " + crop[0])