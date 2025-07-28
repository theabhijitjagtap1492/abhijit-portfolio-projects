import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from PIL import Image

# Load model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("rice_classifier_vgg16.keras")
    return model

model = load_model()

# Class labels (update these based on your dataset)
class_names = [ 'Arborio', 'Basmati', 'Ipsala', 'Jasmine', 'Karacadag']

# App title
st.title("🍚 Rice Grain Classifier (VGG16)")

# File uploader
uploaded_file = st.file_uploader("Upload a rice grain image", type=["jpg", "jpeg", "png"])

# Prediction
if uploaded_file is not None:
    try:
        img = Image.open(uploaded_file).convert('RGB')
        st.image(img, caption="Uploaded Image", use_column_width=True)

        # Preprocess image (resize to match model input, e.g., 224x224 for VGG16)
        img_resized = img.resize((224, 224))
        img_array = image.img_to_array(img_resized)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = tf.keras.applications.vgg16.preprocess_input(img_array)

        # Make prediction
        prediction = model.predict(img_array)
        predicted_class = class_names[np.argmax(prediction)]
        confidence = np.max(prediction)

        st.success(f"Predicted: **{predicted_class}** with {confidence:.2%} confidence")
    except Exception as e:
        st.error(f"⚠️ Error during prediction: {str(e)}")
