import streamlit as st
from PIL import Image

st.title("BMI Calulator App")

weight = st.number_input("What is your weight in KG")
height = st.number_input("What is your height in metres ")



def bmi_c(weight, height):
    bmi = weight / height**2
    bmi = round(bmi,1)
    if bmi > 30:
        rate = "overweight"
    elif 24 < bmi < 29:
        rate = "normalweight"
    else:
        rate = "underweight"
    return(f"Your BMI score is {bmi} and you are at {rate}")
    
if st.button("Calculate BMI"):
    st.write( bmi_c(weight, height))
