import streamlit as st
from streamlit_lottie import st_lottie

placeholder1 = st.empty()
placeholder2 = st.empty()

with placeholder1.container():
    # Title
    st.markdown("<h1 style='text-align: center; color: red;'>Lung Cancer GPT</h1>", unsafe_allow_html=True)

with placeholder2.container():   
    # Vidio
    st_lottie("https://lottie.host/aeb09430-58c1-4cde-9d82-6c22ff410b2e/iWUBJx0EHF.json")

# Button
col1, col2, col3 , col4, col5 = st.beta_columns(5)
with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    center_button = st.button('Button')


# picture = st.camera_input("Take a picture", label_visibility="collapsed")

# if picture:
#     st.image(picture)