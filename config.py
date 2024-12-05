import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "llama2")
EMBEDDINGS_MODEL = os.getenv("EMBEDDINGS_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "vector_db/")
