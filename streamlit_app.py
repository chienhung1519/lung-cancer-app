import streamlit as st
from streamlit_lottie import st_lottie

placeholder = st.empty()

with placeholder.container():
    st_lottie("https://lottie.host/aeb09430-58c1-4cde-9d82-6c22ff410b2e/iWUBJx0EHF.json")


# picture = st.camera_input("Take a picture", label_visibility="collapsed")

# if picture:
#     st.image(picture)