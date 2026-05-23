from fastapi import FastAPI, UploadFile, File, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

import cv2
import numpy as np
import os

from .model import get_model
from .utils import draw_people_only, count_people
from .auth import authenticate_user, create_token
from .deps import get_current_user


# ---------------- APP ----------------
app = FastAPI(title="AI Vision SaaS")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- MODEL ----------------
model = get_model()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "..", "uploads")
OUTPUT_DIR = os.path.join(BASE_DIR, "..", "outputs")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ---------------- LOGIN ----------------
class LoginRequest(BaseModel):
    username: str
    password: str


@app.post("/login")
def login(data: LoginRequest):

    if not authenticate_user(data.username, data.password):
        return {"error": "invalid credentials"}

    token = create_token({"sub": data.username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# ---------------- DETECT (PROTECTED) ----------------
@app.post("/detect")
def detect(file: UploadFile = File(...), user=Depends(get_current_user)):

    contents = file.file.read()

    np_arr = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    results = model(image)

    count = count_people(results)
    annotated = draw_people_only(image, results)

    filename = f"{user}_{file.filename}"
    output_path = os.path.join(OUTPUT_DIR, filename)

    cv2.imwrite(output_path, annotated)

    return {
        "people_count": count,
        "image_url": f"http://127.0.0.1:8000/image/{filename}"
    }


# ---------------- SERVE IMAGE ----------------
@app.get("/image/{filename}")
def get_image(filename: str):
    path = os.path.join(OUTPUT_DIR, filename)
    return FileResponse(path)