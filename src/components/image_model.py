import numpy as np
from keras.models import load_model
from PIL import Image, ImageOps, UnidentifiedImageError
from src.utils.logger import logger
import os
import traceback

# Load model & labels once with exception handling
model = None
class_names = []

try:
    if not os.path.exists("src/models/keras_Model1.h5"):
        raise FileNotFoundError("Model file not found: src/models/keras_Model1.h5")

    if not os.path.exists("src/models/labels.txt"):
        raise FileNotFoundError("Labels file not found: src/models/labels.txt")

    model = load_model("src/models/keras_Model1.h5", compile=False)

    with open("src/models/labels.txt", "r") as f:
        class_names = f.readlines()

    logger.info("✅ Food classification model and labels loaded successfully.")

except Exception as e:
    logger.exception("❌ Failed to load model or labels.")
    traceback.print_exc()
    model = None
    class_names = []


# Pre-allocate data array
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


def classify_image(image_path: str) -> str:
    """
    Run Keras model on image and return predicted class name.
    Returns 'unknown' if classification fails.
    """
    if model is None or not class_names:
        logger.error("⚠️ Model or labels not loaded. Cannot classify.")
        return "unknown"

    try:
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")

        logger.debug(f"Classifying image: {image_path}")

        # Open and preprocess image
        try:
            image = Image.open(image_path).convert("RGB")
        except UnidentifiedImageError:
            logger.error(f"❌ Cannot identify image file: {image_path}")
            return "unknown"

        image = ImageOps.fit(image, (224, 224), Image.LANCZOS)
        image_array = np.asarray(image)

        if image_array.shape != (224, 224, 3):
            raise ValueError(f"Unexpected image shape: {image_array.shape}")

        # Normalize
        normalized = (image_array.astype(np.float32) / 127.5) - 1
        data[0] = normalized

        # Predict
        prediction = model.predict(data)
        index = np.argmax(prediction)

        if index >= len(class_names):
            raise IndexError(f"Predicted index {index} out of range for labels.")

        food_name = class_names[index][2:].strip()
        logger.info(f"Predicted food: {food_name}")
        return food_name

    except Exception as e:
        logger.exception(f"❌ Error during classification for {image_path}")
        traceback.print_exc()
        return "unknown"
