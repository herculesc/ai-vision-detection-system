# 🧠 AI Vision Detection System

A real-time Computer Vision SaaS that detects and counts objects in images using YOLO, FastAPI, and Streamlit.

This project demonstrates a complete end-to-end AI product pipeline — from model inference to API deployment and interactive web interface.

---

## 🚀 What this system does

This system transforms images into actionable insights using Computer Vision.

It can:

- Detect objects using YOLO (People, vehicles, general objects)
- Count detected instances in real time
- Generate annotated images with bounding boxes
- Provide results via REST API (FastAPI)
- Display results in a SaaS-style web interface (Streamlit)

---

## 💡 Why this project matters

This project demonstrates how a Computer Vision system moves from research to production:

- Model inference with YOLO
- Backend API development with FastAPI
- Frontend integration with Streamlit
- Full pipeline deployment architecture
- Real-world AI application design

👉 This is not just a model — it is a deployable AI system.

---

## 🧠 Key Features

- ✅ YOLO-based object detection
- ✅ Real-time image processing
- ✅ Object counting system
- ✅ FastAPI REST backend
- ✅ Streamlit SaaS-style frontend
- ✅ Image upload and visualization
- ✅ Modular and scalable architecture
- ✅ Ready for deployment

---

## 🏗️ System Architecture

```text
User Upload Image
        ↓
Streamlit Frontend (UI Layer)
        ↓
FastAPI Backend (API Layer)
        ↓
YOLO Model Inference (AI Layer)
        ↓
OpenCV Processing (Vision Layer)
        ↓
Return:
- Bounding boxes image
- Object count

# 🧰 Tech Stack

## Backend

* Python
* FastAPI
* Uvicorn

## Computer Vision

* YOLO
* OpenCV
* PyTorch
* Ultralytics

## Frontend

* Streamlit

## Data Processing

* NumPy
* Pillow

---

# 📁 Project Structure

```text
ai-vision-detection-system/
│
├── app/
│   ├── main.py              # FastAPI backend
│   ├── model.py            # YOLO inference logic
│   ├── utils.py            # helper functions
│
├── uploads/               # uploaded images
├── outputs/               # processed images
├── assets/                # demo images & gifs
│
├── streamlit_app.py       # frontend UI
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-vision-detection-system.git
```

---

## 2. Create virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

## Start FastAPI backend

```bash
uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

## Start Streamlit frontend

```bash
streamlit run streamlit_app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

# 🧪 API Example

## Endpoint

```http
POST /count-people
```

---

## Response Example

```json
{
  "people_count": 3,
  "output_image": "outputs/result.jpg"
}
```

---

# 📌 Future Improvements

* Video upload support
* Real-time webcam detection
* Object tracking
* Detection confidence metrics
* Cloud deployment
* Multi-object detection
* User authentication
* Database integration

---

# 💼 Use Cases

* Smart surveillance
* Crowd analysis
* Retail analytics
* Traffic monitoring
* Security systems
* Computer Vision demos
* AI SaaS prototypes

---

# 👨‍💻 Author

## Hércules Carlos Dos Santos Pereira

Machine Learning Engineer and Computer Vision Developer focused on:

* Artificial Intelligence
* Computer Vision
* Deep Learning
* Python APIs
* AI Systems

### Links

* GitHub: [https://github.com/herculesc](https://github.com/herculesc)
* LinkedIn: Add your LinkedIn URL here

---

# ⭐ If you liked this project

Consider giving the repository a star.
