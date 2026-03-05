import streamlit as st
from PIL import Image

st.title("Browse and Display Picture")

picture = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if picture is not None:
    img = Image.open(picture)
    st.image(img, caption="Uploaded Image")
