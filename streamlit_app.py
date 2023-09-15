import streamlit as st

picture = st.camera_input("", label_visibility="hidden")

if picture:
    st.image(picture)