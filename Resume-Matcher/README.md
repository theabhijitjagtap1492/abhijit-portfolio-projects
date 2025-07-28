# 📄 Resume & Job Description Matcher

This is a Streamlit web application that helps you match a resume to a job description based on skill overlap. It calculates a match score, shows which skills from the job description are present in the resume, and which are missing.

## ✨ Features

- **Skill-Based Matching**: Compares the resume and job description based on a predefined list of skills.
- **Match Score**: Calculates a score from 0 to 10 based on how many required skills are met.
- **Detailed Feedback**: Lists the specific skills that matched and those that are missing.
- **Fit for Role**: Provides a simple "Yes" or "No" recommendation based on the score.
- **File Upload**: Supports uploading both the resume and job description as PDF files.

## 🛠️ Setup & Installation

To run this project locally, please follow these steps:

**1. Clone the repository (or download the files):**
```bash
git clone <your-repository-url>
cd resume-matcher
```

**2. Create a virtual environment:**
This keeps your project dependencies separate from your system's Python installation.
```bash
python -m venv venv
```
Activate the environment:
- **On Windows:**
  ```bash
  .\\venv\\Scripts\\activate
  ```
- **On macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

**3. Install the required packages:**
All dependencies are listed in the `requirements.txt` file.
```bash
pip install -r requirements.txt
```

## 🚀 How to Run the Application

Once you have installed the dependencies, you can run the Streamlit app with the following command:

```bash
streamlit run app.py
```

Your web browser should open to the application, ready for you to upload your files!

## 🔧 How It Works

The application works as follows:
1.  **PDF Extraction**: Text is extracted from the uploaded PDF files.
2.  **Skill Extraction**: A predefined list of common skills is used to find which skills are mentioned in the job description and the resume.
3.  **Scoring**: A score is calculated based on the ratio of matched skills to the total skills required in the job description.
4.  **Feedback Generation**: The app generates feedback detailing the matched skills, missing skills, and a final "Fit for Role" assessment. 