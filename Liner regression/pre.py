import streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np

exp = np.array([[2, 18], [2, 16], [4, 16]])  
sal = np.array([75000, 60000, 75000])  
model = LinearRegression().fit(exp, sal)
st.title("Salary Prediction App")

experience = st.number_input("Enter years of experience:", min_value=0, max_value=50, value=0)
education = st.number_input("Enter years of education:", min_value=0, max_value=25, value=18)


if st.button("Predict Salary"):
    prediction = model.predict([[experience, education]])
    st.write("Predicted Salary for" , experience , "years of experience and ", education , "years of education is:", prediction[0])
