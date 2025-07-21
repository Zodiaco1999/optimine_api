from fastapi import FastAPI, UploadFile, File
import numpy as np
import cv2
from services.image_recognition import predict_image
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://localhost",
    "https://localhost:4200",
    "http://localhost",
    "http://localhost:4200",
    "http://127.0.0.1:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    class_name, confidence = predict_image(img)

    return {
        "class": class_name,
        "confidence": confidence
    }