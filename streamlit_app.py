import streamlit as st
from streamlit_lottie import st_lottie

placeholder1 = st.empty()
placeholder2 = st.empty()

with placeholder1.container():
    # Title
    st.markdown("<h1 style='text-align: center; color: blue;'>Lung Cancer GPT</h1>", unsafe_allow_html=True)

with placeholder2.container():   
    # Vidio
    st_lottie("https://lottie.host/aeb09430-58c1-4cde-9d82-6c22ff410b2e/iWUBJx0EHF.json")

# Button
col1, col2, col3 = st.columns(3)
with col1:
    st.write("     ")
with col2:
    center_button = st.button('Take Photo')
with col3 :
    st.write("     ")



# picture = st.camera_input("Take a picture", label_visibility="collapsed")

# if picture:
#     st.image(picture)