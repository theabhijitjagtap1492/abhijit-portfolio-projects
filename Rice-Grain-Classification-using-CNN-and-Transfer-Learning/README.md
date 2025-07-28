# -Rice-Grain-Classification-using-CNN-and-Transfer-Learning
This project aims to build an image classification system that can accurately classify different types of rice grains using a Convolutional Neural Network (CNN). The model leverages transfer learning to adapt pre-trained networks for rice grain classification. The project also includes a user-friendly interface for real-time predictions.
## 📌 Project Overview

- **Objective**: Classify different types of rice grains using deep learning.
- 
- **Approach**:
  - Preprocess and explore the rice grain dataset.
  - Utilize a pre-trained CNN (VGG16) with transfer learning.
  - Evaluate model performance using Accuracy, Precision, Recall, and F1-score.
  - Perform hyperparameter tuning for optimization.
  - Deploy a Gradio-based UI for live image classification.

## 📁 Project Directory Structure

Rice-Grain-Classification-using-CNN/
├── Application demo .png # Screenshot of the working application
├── Flow Diagram.jpeg # Visual flow of the model or app architecture
├── README.md # Project documentation
├── Rice Classifier Pesudo code .txt # Pseudocode of the rice classifier
├── app.py # Main Streamlit app script
├── rice-classifier-model-building.ipynb # Jupyter notebook for training the rice classifier model
├── requirements.txt

## 🗃️ Dataset

- The dataset contains images of 5 rice varieties 
- [📂https://www.kaggle.com/datasets/muratkokludataset/rice-image-dataset](#) 

---
##Library and Dependencies Required for this Project


tensorflow

keras

numpy

pandas

scikit-learn

matplotlib

seaborn

opencv-python

streamlit

Pillow





## 🧠 Model Architecture

- **Base Model**: Pre-trained CNN (VGG16)
- **Layers Added**:
  - Global Average Pooling
  - Dense layers with ReLU and Dropout
  - Final Softmax output layer for classification

---
🚀 Future Improvements


I’m currently working on implementing and evaluating additional models like ResNet and Xception to further enhance the rice grain classification performance.
