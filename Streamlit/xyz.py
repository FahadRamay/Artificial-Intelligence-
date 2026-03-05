import streamlit as st
st.title("MY 1st AI Lab")

salary=st.slider("Select your salary range :", min_value=25000, max_value=200000, value=(30000, 60000), step=5000)
st.write(salary[0],salary[1])

from PIL import Image

st.title("Browse and Display Picture")

picture = st.file_uploader("Choose an image...", type=['jpeg', 'png', 'jpg'])

if picture is not None:
    img = Image.open(picture)
    st.image(img, caption="Uploaded Image")
