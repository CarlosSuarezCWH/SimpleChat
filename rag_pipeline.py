from app.embeddings.faiss_handler import FAISSHandler

class RAGPipeline:
    def __init__(self, model):
        """
        Inicializa el pipeline RAG.
        """
        self.model = model
        self.faiss_handler = FAISSHandler()

    def create_embeddings(self, user_id, text):
        """
        Divide el texto en fragmentos y crea embeddings.
        """
        chunk_size = 500  # Tamaño del fragmento
        chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
        self.faiss_handler.add_to_index(chunks)

    def query(self, user_id, question, top_k=5):
        """
        Recupera contexto y genera respuesta.
        """
        context = " ".join(self.faiss_handler.search(question, top_k))
        prompt = f"Contexto: {context}\nPregunta: {question}\nRespuesta:"
        return self.model.generate(prompt)
