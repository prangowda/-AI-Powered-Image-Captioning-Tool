import tensorflow as tf
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.inception_v3 import preprocess_input

# Load trained model
model = load_model("caption_model.h5")

# Load sample words (Replace with a trained dictionary)
word_dict = {0: "a", 1: "man", 2: "is", 3: "riding", 4: "bike", 5: "."}

def generate_caption(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (299, 299))
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)

    # Dummy prediction (Replace with actual NLP model)
    predicted_words = [word_dict[i] for i in range(6)]
    caption = " ".join(predicted_words)
    return caption

# Test
image_path = "static/sample.jpg"
caption = generate_caption(image_path)
print("Generated Caption:", caption)
