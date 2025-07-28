# 🧠 Loan Prediction using Machine Learning

This project predicts whether a loan application will be approved based on applicant data using classic machine learning models.

---

## 📁 File Descriptions

| File Name | Description |
|-----------|-------------|
| `Loan_Prediction.ipynb`  | Jupyter Notebook containing complete EDA, preprocessing, model training, evaluation, and saving |
| `loan_model.pkl`  | Trained model saved using `pickle` |
| `train_u6lujuX_CVtuZ9i.csv`  | Training dataset with labels |
| `test_Y3wMUE5_7gLdaTN.csv`  | Test dataset for making predictions |
| `Requirements.txt`  | Required libraries to run the notebook or scripts |

---

## 🧠 Features Used for Prediction

- Gender
- Married
- Dependents
- Education
- Self_Employed
- ApplicantIncome
- CoapplicantIncome
- LoanAmount
- Loan_Amount_Term
- Credit_History
- Property_Area

---

## ⚙️ Models Trained

- Logistic Regression  
- Decision Tree  
- Support Vector Machine (SVM)  
- K-Nearest Neighbors (KNN)  
- Naive Bayes  
- ✅ Random Forest (Best performing)

---

## 🔄 Workflow

1. Load and clean the dataset
2. Handle missing values
3. Encode categorical features using `LabelEncoder`
4. Train multiple models and evaluate
5. Save the best model using `pickle`
6. Predict test data and prepare results

---

## 🧪 How to Run

### 1. Clone or Download the Repository

```bash
git clone https://github.com/YOUR_USERNAME/loan-system.git
cd loan-system
