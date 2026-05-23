from ultralytics import YOLO

# predict model

model = YOLO("yolov8n.pt")

def get_model():
    return model