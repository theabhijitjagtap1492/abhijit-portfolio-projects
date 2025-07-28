import cohere
import re
import numpy as np

co = cohere.Client('0vkdA4vIWdawEId6FLlZhckeXGCB6P6c7tmUmrRk')

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

def is_relevant(line):
    # Remove lines that are likely to be names, emails, phone numbers, addresses, headings, companies, or dates
    if len(line.split()) < 3 or len(line.split()) > 30:
        return False
    if re.search(r'\b(name|email|phone|contact|address|curriculum vitae|resume|cv|linkedin|github|profile|pvt|ltd|technologies|solutions|inc|llc|private limited|company|institute|university|college|school|may|june|july|august|september|october|november|december|january|february|march|april|present|\d{4})\b', line, re.I):
        return False
    if re.match(r'^[A-Z\s\&]+$', line) and len(line) < 40:  # All caps headings
        return False
    if re.search(r'\d{10,}', line):  # Long numbers (phone)
        return False
    if re.search(r'@', line):  # Email
        return False
    if re.match(r'^\s*$', line):
        return False
    return True

def chunk_lines(lines):
    # Group lines into chunks of up to 3 lines for more context
    chunks = []
    temp = []
    for line in lines:
        if is_relevant(line):
            temp.append(line)
            if len(temp) == 3:
                chunks.append(' '.join(temp))
                temp = []
    if temp:
        chunks.append(' '.join(temp))
    return chunks

def extract_skills(text):
    text = text.lower()
    found = set()
    for skill in COMMON_SKILLS:
        # Use word boundaries for single words, substring for phrases
        if ' ' in skill:
            if skill in text:
                found.add(skill)
        else:
            if re.search(r'\b' + re.escape(skill) + r'\b', text):
                found.add(skill)
    return found

def generate_feedback(resume, jd):
    # Skill-based feedback
    jd_skills = extract_skills(jd)
    resume_skills = extract_skills(resume)
    matched = sorted(jd_skills & resume_skills)
    missing = sorted(jd_skills - resume_skills)
    if jd_skills:
        score = round(10 * len(matched) / len(jd_skills), 2)
    else:
        score = 0.0
    fit = 'Yes' if score >= 7 else 'No'
    feedback = f"**Score:** {score}/10\n\n"
    feedback += "**Matched Skills (from JD found in Resume):**\n" + '\n'.join(f"- {s}" for s in matched)
    feedback += "\n\n**Missing Skills (from JD not found in Resume):**\n" + '\n'.join(f"- {s}" for s in missing)
    feedback += f"\n\n**Fit for Role:** {fit}"
    return feedback
