import streamlit as st

picture = st.camera_input("Take a picture", label_visibility="hidden")

if picture:
    st.image(picture)