import streamlit as st

picture = st.camera_input("Take a picture", label_visibility="collapsed")

if picture:
    st.image(picture)