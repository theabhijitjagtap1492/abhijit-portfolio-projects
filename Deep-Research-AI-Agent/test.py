# import os
# print("Loaded API Key:", os.getenv("GROQ_API_KEY"))

from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())  # <--- This makes sure it finds the file
