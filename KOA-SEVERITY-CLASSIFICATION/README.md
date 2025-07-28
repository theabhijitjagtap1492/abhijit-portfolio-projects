# KOA-SEVERITY-CLASSIFICATION

# 🦴 Knee Osteoarthritis Severity Classification

This repository contains the final project for the **Complex Data Mining** course at **Savitribai Phule Pune University (SPPU)**.

---

## 📌 Project Overview

Knee osteoarthritis (OA) is a degenerative joint disease caused by the gradual wearing of cartilage. X-ray and MRI imaging are commonly used to assess the loss of joint space and determine the severity of the disease.

This project leverages deep convolutional neural networks (CNNs) to automatically classify the severity of knee osteoarthritis from X-ray images.

---

KOA/
│
├── .venv/                # Virtual environment directory (not pushed to Git)
├── app/                  # Contains main application logic (e.g., Streamlit or Flask app files)
├── assets/               # Static assets like images, icons, logos
├── src/                  # Source code: preprocessing, training, evaluation
│
├── app.py                # Main entry point script to run the application
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation (you’ll create this)


## 🩻 Osteoarthritis Severity - KL Score

The **Kellgren and Lawrence (KL)** grading system is used to assess OA severity in five levels:

| Grade | Description |
|-------|-------------|
| 0     | Healthy     |
| 1     | Doubtful    |
| 2     | Minimal     |
| 3     | Moderate    |
| 4     | Severe      |

> 📸 The dataset used in this project includes labeled X-ray images corresponding to these grades.

---

## 🚀 Features

- ✅ Deep learning-based classification using CNN architectures
- ✅ Ensemble models using accuracy- and F1-score-based weighting
- ✅ Visualization of confusion matrices for performance insight
- ✅ Streamlit-based web app for interactive inference
- ✅ Easy image-based inference via CLI

---


