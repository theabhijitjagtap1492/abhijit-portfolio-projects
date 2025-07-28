import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image

def make_gradcam_heatmap(grad_model, img_array, pred_index=None):
    with tf.GradientTape() as tape:
        last_conv_layer_output, preds = grad_model(img_array)
        if pred_index is None:
            pred_index = tf.argmax(preds[0])
        class_channel = preds[:, pred_index]

    grads = tape.gradient(class_channel, last_conv_layer_output)
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))

    last_conv_layer_output = last_conv_layer_output[0]
    heatmap = last_conv_layer_output @ pooled_grads[..., tf.newaxis]
    heatmap = tf.squeeze(heatmap)

    heatmap = tf.maximum(heatmap, 0) / tf.math.reduce_max(heatmap)
    return heatmap.numpy()

def save_and_display_gradcam(img, heatmap, alpha=0.4):
    heatmap = np.uint8(255 * heatmap)
    jet = cm.get_cmap("jet")
    jet_colors = jet(np.arange(256))[:, :3]
    jet_heatmap = jet_colors[heatmap]

    jet_heatmap = tf.keras.preprocessing.image.array_to_img(jet_heatmap)
    jet_heatmap = jet_heatmap.resize((img.shape[1], img.shape[0]))
    jet_heatmap = tf.keras.preprocessing.image.img_to_array(jet_heatmap)

    superimposed_img = jet_heatmap * alpha + img
    superimposed_img = tf.keras.preprocessing.image.array_to_img(
        superimposed_img
    )
    return superimposed_img

icon = Image.open("app/img/NGI.jpg")
st.set_page_config(
    page_title="Severity Analysis of Arthrosis in the Knee",
    page_icon=icon,
)

class_names = ["Healthy", "Doubtful", "Minimal", "Moderate", "Severe"]
target_size = (224, 224)

model = tf.keras.models.load_model("./model/model_Xception_ft.hdf5")

grad_model = tf.keras.models.clone_model(model)
grad_model.set_weights(model.get_weights())
grad_model.layers[-1].activation = None
grad_model = tf.keras.models.Model(
    inputs=[grad_model.inputs],
    outputs=[
        grad_model.get_layer("global_average_pooling2d_1").input,
        grad_model.output,  # Predictions
    ],
)

# Sidebar
with st.sidebar:
     # 🔰 College Logo
    st.image(r"C:\Users\Admin\Desktop\Test App\app\img\NGI.jpg", width=150)  # Make sure the file is in the same directory as app.py
    st.markdown("### 👨‍🎓 Developed By:")
    st.markdown("- Akash Hede  \n- Abhijit Jagtap  \n- Viraj Bodke  \n- Aniruddha Bambole")

    st.markdown("---")
    st.markdown("## 📂 Upload an X-ray Image")
    uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
    st.markdown("---")
    st.markdown("### ℹ️ About This App")
    st.write("This application analyzes knee X-ray images to determine the severity of arthrosis using Deep Learning.")
    st.markdown("---")

# Main Page
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>Knee Arthrosis Severity Analysis</h1>", unsafe_allow_html=True)

if uploaded_file is not None:
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("### 🖼️ Uploaded X-ray")
        st.image(uploaded_file, use_column_width=True)
        img = tf.keras.preprocessing.image.load_img(uploaded_file, target_size=target_size)
        img = tf.keras.preprocessing.image.img_to_array(img)
        img_aux = img.copy()

        if st.button("🔍 Analyze X-ray", use_container_width=True):
            with st.spinner("Processing image..."):
                img_array = np.expand_dims(img_aux, axis=0)
                img_array = np.float32(img_array)
                img_array = tf.keras.applications.xception.preprocess_input(img_array)
                y_pred = model.predict(img_array)
                y_pred_percentage = 100 * y_pred[0]
                predicted_class_index = np.argmax(y_pred_percentage)
                predicted_class = class_names[predicted_class_index]
                probability = y_pred_percentage[predicted_class_index]

            st.markdown(f"### ✅ **Severity Grade:** {predicted_class}")
            st.markdown(f"### 📊 **Probability:** {probability:.2f}%")

    with col2:
        if 'y_pred_percentage' in locals():
            st.markdown("### 🔥 Heatmap Visualization")
            heatmap = make_gradcam_heatmap(grad_model, img_array)
            image = save_and_display_gradcam(img, heatmap)
            st.image(image, use_column_width=True)

            st.markdown("### 📈 Probability Distribution")
            fig, ax = plt.subplots(figsize=(8, 4))
            colors = ['#3498DB', '#2ECC71', '#F1C40F', '#E67E22', '#E74C3C']
            bars = ax.barh(class_names, y_pred_percentage, height=0.6, align="center", color=colors)
            for bar, p in zip(bars, y_pred_percentage):
                ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2, f"{p:.2f}%", va='center', fontsize=11)
            ax.grid(axis="x", linestyle='--', alpha=0.6)
            ax.set_xlim([0, 120])
            ax.set_xticks(range(0, 101, 20))
            ax.set_xlabel("Probability (%)", fontsize=12)
            ax.set_ylabel("Severity Grade", fontsize=12)
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.tick_params(axis='both', which='major', labelsize=11)
            fig.tight_layout()
            st.pyplot(fig)
        else:
            st.info("Please upload and analyze an X-ray image.")
else:
    st.warning("⚠️ Please upload an X-ray image to start the analysis.")
