# 🧠 AI Vision SaaS — People Detection System

A full-stack Computer Vision SaaS application that detects and counts people in images using **YOLO, FastAPI, and Streamlit**, with **JWT authentication and secure API access**.

This project demonstrates a production-style AI system with authentication, API protection, and a modern web interface.

---

## 🚀 What this system does

This system turns image uploads into structured AI insights in real time.

It can:

* 🔐 Authenticate users using JWT tokens
* 🧠 Detect people in images using YOLO
* 🔢 Count detected objects in real time
* 🖼️ Generate annotated images with bounding boxes
* 🌐 Serve results via REST API (FastAPI)
* 💻 Provide a SaaS-style web interface (Streamlit)
* 🔒 Protect AI endpoints with authentication

---

## 🔥 New Features (SaaS Upgrade)

Compared to a basic AI demo, this version includes:

* 🔐 Login system (JWT authentication)
* 🛡️ Protected API endpoints (/detect secured)
* 👤 Session-based frontend authentication
* 🚪 Logout functionality
* 🌐 REST API architecture (frontend/backend separation)
* 📦 Image storage system (uploads & outputs)
* 🔗 Image serving via API URL
* 💼 SaaS-ready structure

---

## 💡 Why this project matters

This project simulates a real-world AI SaaS product architecture:

* AI model is isolated from UI
* Backend exposes secure API endpoints
* Frontend consumes API like a real product
* Authentication layer protects resources
* System is modular and scalable

👉 This is a deployable AI SaaS prototype.

---

## 🧠 Key Features

* ✅ YOLO-based object detection
* ✅ People counting system
* ✅ JWT authentication system
* ✅ Secure FastAPI backend
* ✅ Streamlit SaaS frontend
* ✅ Image upload and processing
* ✅ Protected AI endpoints
* ✅ Modular architecture (production-style)
* ✅ REST API communication

---

## 🏗️ System Architecture

```text
User
   ↓
Streamlit Frontend (Login + UI)
   ↓
JWT Authentication Request
   ↓
FastAPI Backend (/login)
   ↓
JWT Token Issued
   ↓
User uploads image
   ↓
Streamlit → /detect (with JWT token)
   ↓
FastAPI validates token
   ↓
YOLO Model Inference
   ↓
OpenCV Image Processing
   ↓
Save annotated image
   ↓
Return:
- People count
- Image URL

```

---

## 🔐 Authentication Flow

```text
Login Request
   ↓
FastAPI verifies credentials
   ↓
JWT token generated
   ↓
Token stored in Streamlit session
   ↓
Token sent in Authorization header
   ↓
Backend validates token on /detect
```

---

## 🧰 Tech Stack

### Backend

* Python
* FastAPI
* Uvicorn
* Python-JOSE (JWT)
* Passlib (bcrypt)

### Computer Vision

* YOLO (Ultralytics)
* OpenCV
* PyTorch
* NumPy

### Frontend

* Streamlit

### System Design

* REST API architecture
* JWT authentication
* Stateless backend design

---

## 📁 Project Structure

```text
ai-vision-saas/
│
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI entry point
│   │   ├── auth.py          # JWT authentication logic
│   │   ├── deps.py          # token validation dependency
│   │   ├── model.py         # YOLO model loader
│   │   ├── utils.py         # image processing helpers
│   │
│   ├── uploads/             # uploaded images
│   ├── outputs/             # processed images
│
├── frontend/
│   ├── streamlit_app.py     # SaaS UI (login + dashboard)
│
├── requirements.txt
├── .env                     # secret keys (JWT)
├── README.md
```

---

## ⚙️ Installation

### 1. Clone repository

```bash
git clone https://github.com/yourusername/ai-vision-saas.git
cd ai-vision-saas
```

---

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Start backend

```bash
uvicorn backend.app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

Docs:

```text
http://127.0.0.1:8000/docs
```

---

### Start frontend

```bash
streamlit run frontend/streamlit_app.py
```

Frontend:

```text
http://localhost:8501
```

---

## 🧪 API Endpoints

### 🔐 Login

```http
POST /login
```

Request:

```json
{
  "username": "admin",
  "password": "1234"
}
```

Response:

```json
{
  "access_token": "jwt_token_here",
  "token_type": "bearer"
}
```

---

### 🧠 Detect People (Protected)

```http
POST /detect
Authorization: Bearer <token>
```

Response:

```json
{
  "people_count": 3,
  "image_url": "http://127.0.0.1:8000/image/file.jpg"
}
```

---

## 📌 Future Improvements

* 📊 User dashboard (history of uploads)
* 🧾 Database integration (PostgreSQL)
* ☁️ Cloud deployment (AWS / Render)
* 📹 Video detection support
* 👥 Multi-user SaaS system
* 💳 Payment system (Stripe)
* 📈 Usage limits per user
* 📦 Docker deployment

---

## 💼 Use Cases

* Smart surveillance systems
* Crowd analysis tools
* Retail analytics
* Traffic monitoring
* Security AI systems
* AI SaaS prototypes
* Freelancer product demos (Fiverr / Upwork)

---

## 👨‍💻 Author

**Hércules Carlos**

Machine Learning Engineer focused on:

* Computer Vision
* Deep Learning
* AI Systems
* Backend Development (FastAPI)

GitHub: [https://github.com/herculesc](https://github.com/herculesc)

---

## ⭐ If you like this project

Give it a ⭐ on GitHub — it helps a lot.

👉 transformar isso em **portfólio que converte cliente (Fiverr/Upwork)**
👉 ou montar versão “produto real com deploy + domínio”
