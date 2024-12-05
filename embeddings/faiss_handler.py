from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class FAISSHandler:
    def __init__(self):
        """
        Inicializa el índice FAISS y el modelo de embeddings.
        """
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')  # Modelo ligero
        self.faiss_index = faiss.IndexFlatL2(384)  # Dimensión 384 para MiniLM
        self.embedded_texts = []

    def add_to_index(self, texts):
        """
        Añade textos al índice FAISS.
        """
        embeddings = self.embedding_model.encode(texts, batch_size=32, show_progress_bar=True)
        self.faiss_index.add(np.array(embeddings))
        self.embedded_texts.extend(texts)

    def search(self, query, top_k=5):
        """
        Busca los textos más relevantes en el índice.
        """
        query_embedding = self.embedding_model.encode([query])
        distances, indices = self.faiss_index.search(query_embedding, top_k)
        return [self.embedded_texts[i] for i in indices[0]]
