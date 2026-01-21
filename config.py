import os
from dotenv import load_dotenv
load_dotenv()

# ---------- Vertex AI ----------
PROJECT_ID = os.getenv("PROJECT_ID", "indigo-skyline-463722-s0")
LOCATION = os.getenv("LOCATION", "us-central1")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.0-flash")

# ---------- MySQL ----------
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "port": int(os.getenv("DB_PORT", 3306))
}
