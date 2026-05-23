import streamlit as st
import requests
from PIL import Image

st.set_page_config(
    page_title="AI Vision SaaS",
    page_icon="🧠",
    layout="wide"
)

# HEADER
st.title("🧠 AI Vision Detection System")
st.caption("Detect objects and count people using Computer Vision + YOLO")

API_URL = "http://127.0.0.1:8000/count-people"

# SIDEBAR (estilo SaaS)
st.sidebar.title("⚙️ Settings")
st.sidebar.info("Upload an image to run AI detection")

uploaded_file = st.file_uploader(
    "📤 Upload Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    col1, col2 = st.columns(2)

    # LEFT - ORIGINAL
    with col1:
        st.markdown("### 📷 Original Image")
        image = Image.open(uploaded_file)
        st.image(image, use_container_width=True)

    # RUN BUTTON
    st.markdown("---")

    if st.button("🚀 Run AI Detection"):

        with st.spinner("🧠 Running AI model... please wait"):

            response = requests.post(
                API_URL,
                files={
                    "file": (
                        uploaded_file.name,
                        uploaded_file.getvalue(),
                        uploaded_file.type
                    )
                }
            )

        if response.status_code == 200:
            data = response.json()
            #print(data)

            # RIGHT - RESULTS
            with col2:

                st.markdown("### 🖼️ Processed Image")
                

                try:
                    processed_image = Image.open(data["output_image"])
                    st.image(processed_image, use_container_width=True)
                except:
                    st.warning("Processed image not found")
                    

                st.markdown("### 🧠 AI Results")

                # KPI STYLE
                st.markdown(
                    f"""
                    <div style="
                        background-color:#0f172a;
                        padding:20px;
                        border-radius:12px;
                        text-align:center;
                    ">
                        <h1 style="color:#00ff99; margin:0;">
                            {data['people_count']}
                        </h1>
                        <p style="color:white; margin:5px 0 0 0;">
                            People Detected
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
                



        else:
            st.error("❌ API Error - Check backend")