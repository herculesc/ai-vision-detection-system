# 🧠 AI Vision Detection System

Computer Vision system built with Python, FastAPI, YOLO and Streamlit for real-time people detection and counting.

This project demonstrates a complete AI application pipeline, including:

* Computer Vision inference with YOLO
* FastAPI backend API
* Interactive Streamlit frontend
* Image upload and processing
* Object detection visualization
* SaaS-style interface

---

# 📸 Demo

## 🖼️ Application Interface

> Add screenshots of your application here.

### Original Image

```text
assets/original_image.png
```

![Original Image](assets/original_image.png)

---

### Processed Detection Result

```text
assets/detection_result.png
```

![Detection Result](assets/detection_result.png)

---

# 🎥 Video Demo

> Add a demo video/GIF of the system running.

## Example:

```text
assets/demo.gif
```

![Demo Video](assets/demo.gif)

You can also add a YouTube demo link:

```text
https://youtube.com/your-demo-link
```

---

# 🚀 Features

* ✅ People detection using YOLO
* ✅ FastAPI backend
* ✅ Streamlit SaaS-style frontend
* ✅ Image upload support
* ✅ Object counting
* ✅ Processed image visualization
* ✅ REST API integration
* ✅ Modular project structure

---

# 🏗️ System Architecture

```text
Frontend (Streamlit)
        ↓
FastAPI REST API
        ↓
YOLO Computer Vision Model
        ↓
OpenCV Processing
        ↓
Detection Results + Visualization
```

---

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
│   ├── main.py
│   ├── model.py
│   ├── utils.py
│
├── uploads/
├── outputs/
├── assets/
│
├── streamlit_app.py
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
