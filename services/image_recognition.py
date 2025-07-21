from tensorflow.keras.models import load_model
import numpy as np
import cv2

# Cargar modelo y etiquetas una sola vez
model = load_model("keras_Model.h5", compile=False)
class_names = open("labels.txt", "r").readlines()

def predict_image(image: np.ndarray) -> tuple[str, float]:
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
    image = (image / 127.5) - 1

    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()
    confidence_score = float(prediction[0][index])

    return class_name, confidence_score
