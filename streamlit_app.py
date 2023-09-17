import streamlit as st
from streamlit_lottie import st_lottie

placeholder = st.empty()

with placeholder.container():
    # Title
    col1, col2, col3 = st.columns(3)
    with col2:
        st.header("Lun Cancer GPT")
    
    # Vidio
    st_lottie("https://lottie.host/aeb09430-58c1-4cde-9d82-6c22ff410b2e/iWUBJx0EHF.json")

    # Button
    col1, col2, col3 = st.columns(3)
    with col2:
        st.button("Take photo")


# picture = st.camera_input("Take a picture", label_visibility="collapsed")

# if picture:
#     st.image(picture)