import numpy as np
import joblib
from PIL import Image, ImageOps

def predict(img):
    img = Image.fromarray(img).convert('L')
    img = img.resize((150, 150))
    img_array = np.array(img).reshape((1,150, 150, 1)) / 255.0

    # print(img_array)

    model=joblib.load("model/model.joblib")
    if model is None:
        raise ValueError("Model could not be loaded. Please check the model file and path.")
    prediction = model.predict(img_array)

    # Apply the threshold
    confidence_score = prediction[0][0]  # Assuming the model outputs a single value
    predicted_class = 1 if confidence_score > 0.95 else 0

    print(f"Confidence Score: {confidence_score:.4f}")
    print(f"Predicted Class: {predicted_class}")

    return predicted_class