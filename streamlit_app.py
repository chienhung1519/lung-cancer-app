import base64
from io import BytesIO
from pathlib import Path
from typing import Optional
import time

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
    # b64_data: Optional[str] = _component_func(key=key)

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
                st.experimental_rerun()

elif st.session_state.page == 2:
        
    with placeholder1.container():
        # image = back_camera_input()
        image = st.camera_input("Take a picture")
        if image is not None:
            st.session_state["image"] = image
            st.session_state["page"] = 3
            st.experimental_rerun()

elif st.session_state.page == 3:

    with placeholder1.container():
        st.image(st.session_state["image"])

    with placeholder3.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            back_button = st.button("Take Photo")
            if back_button:
                st.session_state["page"] = 2
                st.experimental_rerun()
        with col3:
            next_button = st.button("Analyze")
            if next_button:
                st.session_state["page"] = 4
                with placeholder2.container():
                    progress_text = "Analyzing. Please wait."
                    my_bar = st.progress(0, text=progress_text)

                    for percent_complete in range(100):
                        time.sleep(0.1)
                        my_bar.progress(percent_complete + 1, text=progress_text)

                    st.session_state["page"] = 4
                    st.experimental_rerun()

# elif st.session_state.page == 4:
#     with placeholder1.container():
#         progress_text = "Analyzing. Please wait."
#         my_bar = st.progress(0, text=progress_text)

#         for percent_complete in range(100):
#             time.sleep(0.1)
#             my_bar.progress(percent_complete + 1, text=progress_text)

#         st.session_state["page"] = 5
#         st.experimental_rerun()

elif st.session_state.page == 4:
    with placeholder1.container():
        st.markdown("<h1 style='text-align: center; color: blue;'>Report Summary</h1>", unsafe_allow_html=True)
        st.info("The patient has been diagnosed with adenocarcinoma in situ in the middle lobe of the right lung, following a robotic wedge resection. The tumor is 1.8 cm in size and is considered unifocal and nonmucinous. The histologic type is adenocarcinoma in situ, nonmucinous. The tumor has not invaded the visceral pleura and no lymph-vascular invasion was identified. The closest margin is 1.0 cm. The patient's primary tumor is pTis, and regional lymph nodes are pNX. No distant metastasis was identified, and the TNM stage groupings are pSage 0 pTisNX.")
        
        st.markdown("<h1 style='text-align: center; color: blue;'>Survival</h1>", unsafe_allow_html=True)
        st.warning("5 years")

        expander = st.expander("Clinical Trials")
        expander.write("[https://clinicaltrials.gov/ct2/show/NCT00003829](https://clinicaltrials.gov/ct2/show/NCT00003829)")

        col1, col2, col3 = st.columns(3)
        with col2:
            back_button = st.button("Take Another Photo")
            if back_button:
                st.session_state["page"] = 2
                st.experimental_rerun()