import streamlit as st

st.title("SUm of 2 numbers")

name = st.text_input('Enter your name')

num1=st.number_input("enter 1st number")
num2=st.number_input("enter 2st number")
if st.button("calculate"):
    st.write(num1+num2)
    st.balloons()
