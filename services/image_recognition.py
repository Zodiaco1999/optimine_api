from tensorflow.keras.models import load_model
import numpy as np
import cv2
from models.predict_response import PredictResponse
from models.replacement import known_replacements

model = load_model("data/keras_model.h5", compile=False)
class_names = open("data/labels.txt", "r").readlines()

def predict_image(image: np.ndarray) -> PredictResponse:
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
    image = (image / 127.5) - 1

    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()
    confidence_score = float(prediction[0][index])
    confidence_pct = round(confidence_score * 100, 2)

    if class_name.lower() == "2 desconocido":
        return PredictResponse(
            confidence_score=confidence_pct,
            replacement=None,
            is_success=False
        )

    replacement = next(
        (r for r in known_replacements if r.label.lower() == class_name.lower()),
        None
    )

    return PredictResponse(
        confidence_score=confidence_pct,
        replacement=replacement,
        is_success=replacement is not None
    )