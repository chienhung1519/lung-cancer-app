import base64
from io import BytesIO
from pathlib import Path
from typing import Optional
import time
import os
import requests

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

def parse_unstructured_data(file_path):
    url = 'https://api.unstructured.io/general/v0/general'
    headers = {
        'accept': 'application/json',
        'unstructured-api-key': st.secrets['UNSTRUCTURED_API_KEY'],
    }

    data = {'strategy': 'auto',}
    file_data = {'files': open(file_path, 'rb')}

    response = requests.post(url, headers=headers, data=data, files=file_data)
    json_response = response.json()

    return json_response

placeholder1 = st.empty()
placeholder2 = st.empty()
placeholder3 = st.empty()
placeholder4 = st.empty()

if st.session_state.page == 1:
    
    with placeholder1.container():
        # Title
        st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>LungGPT</h1>", unsafe_allow_html=True)

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
                st.rerun()

    # File Uploader
    with placeholder4.container():
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            st.session_state["page"] = 5
            with open("test.pdf", 'wb') as f:
                f.write(uploaded_file.getvalue())
            st.rerun()

elif st.session_state.page == 2:
        
    with placeholder1.container():
        # image = back_camera_input()
        image = st.camera_input("Take a picture")
        if image is not None:
            st.session_state["image"] = image
            st.session_state["page"] = 3
            with open ('test.jpg','wb') as file:
                file.write(image.getbuffer())
            st.rerun()

elif st.session_state.page == 3:

    file_path = 'test.jpg'
    json_response = parse_unstructured_data(file_path)

    with placeholder1.container():
        st.image(file_path)

    with placeholder2.container():
        st.info("\n".join([res["text"] for res in json_response]))

    with placeholder3.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            back_button = st.button("Take Photo")
            if back_button:
                st.session_state["page"] = 2
                st.rerun()
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
                    st.rerun()

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
        st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>Report Summary</h1>", unsafe_allow_html=True)
        st.info("Overall, the patient's pathology reveals a histology subtype of ADC (Adenocarcinoma) with a predominant lepidic pattern. The PD-L1 expression was tested using the 22C3 assay, showing a tumor proportion score (TPS) of 0%. Among the driver mutations tested, the presence of CK7 and TTF-1 was detected. The tumor staging according to post-surgical assessment indicates a primary tumor of T4 category, and the status of regional lymph nodes (pN) is unknown (Nx). Additionally, distant metastasis (pM) is observed in the form of M1a category. Consequently, the patient's overall stage is classified as IVA.")
        
        st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>Survival</h1>", unsafe_allow_html=True)
        st.warning("1.5 years")

        expander = st.expander("Clinical Trials")
        expander.write("[https://www1.cde.org.tw/ct_taiwan/search_case2.php?caseno_ind%5B1%5D=14094](https://www1.cde.org.tw/ct_taiwan/search_case2.php?caseno_ind%5B1%5D=14094)")

        col1, col2, col3 = st.columns(3)
        with col2:
            back_button = st.button("Take Another Photo")
            if back_button:
                st.session_state["page"] = 2
                st.rerun()

elif st.session_state.page == 5:

    file_path = 'test.pdf'
    json_response = parse_unstructured_data(file_path)

    with placeholder2.container():
        st.info("\n".join([res["text"] for res in json_response]))

    with placeholder3.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            back_button = st.button("Back")
            if back_button:
                st.session_state["page"] = 1
                st.rerun()
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
                    st.rerun()