import streamlit as st
import requests
from PIL import Image

API = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Vision SaaS",
    page_icon="🧠",
    layout="wide"
)

# ---------------- SESSION ----------------
if "token" not in st.session_state:
    st.session_state.token = None


# ===================== LOGIN =====================
if not st.session_state.token:



    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.title("🔐 AI Vision SaaS Login")
        st.caption("Secure access to AI detection system")

        user = st.text_input("User")
        password = st.text_input("Password", type="password")

        if st.button("Login", use_container_width=True):

            res = requests.post(
                f"{API}/login",
                json={
                    "username": user,
                    "password": password
                }
            )

            if res.status_code == 200:
                data = res.json()

                if "access_token" in data:
                    st.session_state.token = data["access_token"]
                    st.rerun()
                else:
                    st.error(data)
            else:
                st.error(res.text)


# ===================== APP =====================
else:

    # -------- HEADER STYLE ANTIGO + LOGOUT --------
    col_title, col_logout = st.columns([8, 1])

    with col_title:
        st.title("🧠 AI Vision Detection System")
        st.caption("Detect objects and count people using Computer Vision + YOLO")

    with col_logout:
        st.write("")
        if st.button("🚪 Logout"):
            st.session_state.token = None
            st.rerun()

    st.divider()

    # ---------------- SIDEBAR ----------------
    st.sidebar.title("⚙️ Settings")
    st.sidebar.info("Upload an image to run AI detection")

    uploaded_file = st.file_uploader(
        "📤 Upload Image",
        type=["jpg", "jpeg", "png"]
    )

    # ---------------- MAIN UI ----------------
    if uploaded_file:

        col1, col2 = st.columns(2)

        # LEFT - ORIGINAL (igual interface antiga)
        with col1:
            st.markdown("### 📷 Original Image")
            image = Image.open(uploaded_file)
            st.image(image, use_container_width=True)

        st.markdown("---")

        if st.button("🚀 Run AI Detection", use_container_width=True):

            with st.spinner("🧠 Running AI model... please wait"):

                res = requests.post(
                    f"{API}/detect",
                    files={
                        "file": (
                            uploaded_file.name,
                            uploaded_file.getvalue(),
                            uploaded_file.type
                        )
                    },
                    headers={"Authorization": f"Bearer {st.session_state.token}"}
                )

            if res.status_code == 200:
                data = res.json()

                with col2:
                    st.markdown("### 🖼️ Processed Image")

                    st.image(
                        data["image_url"],
                        use_container_width=True
                    )

                    st.markdown("### 🧠 AI Results")

                    st.markdown(
                        f"""
                        <div style="
                            background-color:#0f172a;
                            padding:25px;
                            border-radius:12px;
                            text-align:center;
                            box-shadow:0px 4px 12px rgba(0,0,0,0.25);
                        ">
                            <h1 style="color:#00ff99; margin:0; font-size:48px;">
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