import streamlit as st
number=st.number_input("")
name=st.text_input("")
slider=st.slider('enter range', min_value=100, max_value=1000, value=(500,580),step=10)
if st.button('press'):
    st.write(slider[0],slider[1])
