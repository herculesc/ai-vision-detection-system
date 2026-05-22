from fastapi import FastAPI, UploadFile, File
import cv2
import shutil
import os

from app.model import get_model
from app.utils import draw_people_only, count_people
import numpy as np

app = FastAPI(title="People Counter API")

model = get_model()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


@app.post("/count-people")
async def count_people_endpoint(file: UploadFile = File(...)):

    contents = await file.read()

    np_arr = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    if image is None:
        return {"error": "Invalid image file"}

    results = model(image)

    people_count = count_people(results)

    annotated_image = draw_people_only(image, results)

    output_path = f"{OUTPUT_DIR}/people_{file.filename}"
    cv2.imwrite(output_path, annotated_image)

    return {
        "people_count": people_count,
        "output_image": output_path
    }