import base64
from io import BytesIO
from pathlib import Path
from typing import Optional

import streamlit.components.v1 as components
import streamlit as st
from streamlit_lottie import st_lottie

# Initialization
if "page" not in st.session_state:
    st.session_state["page"] = 1

if "image" not in st.session_state:
    st.session_state["image"] = None

st.write('''<style>

[data-testid="column"] {
    width: calc(33.3333% - 1rem) !important;
    flex: 1 1 calc(33.3333% - 1rem) !important;
    min-width: calc(33% - 1rem) !important;
}
</style>''', unsafe_allow_html=True)

# Tell streamlit that there is a component called camera_input_live,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend").absolute()
_component_func = components.declare_component(
    "back_camera_input", path=str(frontend_dir)
)

def back_camera_input(
    height: int = 450,
    width: int = 500,
    key: Optional[str] = None,    
) -> Optional[BytesIO]:
    """
    Add a descriptive docstring
    """
    b64_data: Optional[str] = _component_func(
        height=height,
        width=width,
        key=key,
    )

    if b64_data is None:
        return None

    raw_data = b64_data.split(",")[1]  # Strip the data: type prefix

    component_value = BytesIO(base64.b64decode(raw_data))

    return component_value

placeholder1 = st.empty()
placeholder2 = st.empty()
placeholder3 = st.empty()

if st.session_state.page == 1:
    
    with placeholder1.container():
        # Title
        st.markdown("<h1 style='text-align: center; color: blue;'>Lung Cancer GPT</h1>", unsafe_allow_html=True)

    with placeholder2.container():   
        # Vidio
        st_lottie("https://lottie.host/aeb09430-58c1-4cde-9d82-6c22ff410b2e/iWUBJx0EHF.json")

    # Button
    with placeholder3.container():
        col1, col2, col3 = st.columns(3)
        with col2:
            home_button = st.button('Take Photo')
            if home_button:
                st.session_state["page"] = 2

elif st.session_state.page == 2:
        
    with placeholder1.container():
        image = back_camera_input()
        if image is not None:
            st.session_state["image"] = image
            st.session_state["page"] = 3

elif st.session_state.page == 3:

    st.image(st.session_state["image"])

    col1, col2, col3 = st.columns(3)
    with col1:
        back_button = st.button("Take Photo")
        if back_button:
            st.session_state["page"] = 2
    with col3:
        next_button = st.button("Analyze")
        if next_button:
            st.session_state["page"] = 4

elif st.session_state.page == 4:
    st.write("Page 4")



# picture = st.camera_input("Take a picture", label_visibility="collapsed")

# if picture:
#     st.image(picture)