import tensorflow as tf
from tensorflow.keras.layers import LSTM, Embedding, Dense, Dropout, Bidirectional
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.models import Model
import numpy as np
import pickle

# Load pre-trained CNN model (InceptionV3)
def build_feature_extractor():
    model = InceptionV3(weights="imagenet")
    model = Model(inputs=model.input, outputs=model.layers[-2].output)
    return model

feature_extractor = build_feature_extractor()

# Define LSTM Model for Captioning
def build_captioning_model(vocab_size, max_length):
    inputs = tf.keras.Input(shape=(2048,))
    x = Dense(256, activation="relu")(inputs)
    x = Dropout(0.5)(x)
    x = Dense(vocab_size, activation="softmax")(x)
    model = Model(inputs, outputs)
    return model

model = build_captioning_model(vocab_size=5000, max_length=20)
model.compile(loss="categorical_crossentropy", optimizer="adam")

# Save trained model
model.save("caption_model.h5")
print("Model trained and saved successfully!")
