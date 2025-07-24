from fastapi import FastAPI, UploadFile, File, Query
import numpy as np
import cv2
from services.ia_chat import answer_question
from services.image_recognition import predict_image
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://localhost",
    "https://localhost:4200",
    "http://localhost",
    "http://localhost:4200",
    "http://127.0.0.1:4200",
    "https://zodiaco1999.github.io",
    "https://zodiaco1999",
    "http://zodiaco1999.github.io",
    "http://zodiaco1999"
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

    return predict_image(img)

@app.get("/ask")
def ask(text: str = Query(..., description="Pregunta relacionada con retroexcavadoras o palas hidráulicas")):
    return answer_question(text)