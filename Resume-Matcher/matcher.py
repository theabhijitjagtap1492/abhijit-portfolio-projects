import re

# A basic list of common data/tech skills (expand as needed)
COMMON_SKILLS = [
    'python', 'java', 'c++', 'c#', 'sql', 'nosql', 'mongodb', 'mysql', 'postgresql', 'oracle',
    'excel', 'tableau', 'powerbi', 'pandas', 'numpy', 'scipy', 'matplotlib', 'seaborn',
    'tensorflow', 'keras', 'pytorch', 'scikit-learn', 'sklearn', 'fastapi', 'flask', 'django',
    'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'git', 'github', 'bitbucket',
    'linux', 'bash', 'shell', 'hadoop', 'spark', 'hive', 'pig', 'airflow',
    'machine learning', 'deep learning', 'nlp', 'natural language processing',
    'cnn', 'rnn', 'lstm', 'ann', 'xgboost', 'lightgbm', 'catboost',
    'data analysis', 'data visualization', 'data mining', 'data wrangling',
    'statistics', 'regression', 'classification', 'clustering', 'reinforcement learning',
    'computer vision', 'opencv', 'matlab', 'sas', 'r', 'json', 'xml', 'api',
    'html', 'css', 'javascript', 'react', 'angular', 'node', 'typescript',
    'faiss', 'vector database', 'retrieval-augmented generation', 'rag',
]

def extract_skills(text):
    text = text.lower()
    found = set()
    for skill in COMMON_SKILLS:
        # Use word boundaries for single words, substring for phrases
        if ' ' in skill:
            if skill in text:
                found.add(skill)
        else:
            if re.search(r'\\b' + re.escape(skill) + r'\\b', text):
                found.add(skill)
    return found

def get_resume_match_score(resume, jd):
    jd_skills = extract_skills(jd)
    resume_skills = extract_skills(resume)
    if jd_skills:
        score = round(10 * len(jd_skills & resume_skills) / len(jd_skills), 2)
    else:
        score = 0.0
    return score
