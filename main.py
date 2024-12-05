import sys
import os
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from app.config import MODEL_NAME
from app.pdf_processing import process_pdf
from app.rag_pipeline import RAGPipeline
from app.models.model_selector import load_model
import uvicorn

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Crear la instancia de FastAPI
app = FastAPI()

# Cargar el modelo según la configuración
model = load_model()
rag_pipeline = RAGPipeline(model)

@app.post("/process-pdf/")
async def process_pdf_endpoint(
    pdf: UploadFile = File(...), user_id: str = Form(...)
):
    """
    Endpoint para procesar un PDF. Recibe el archivo y el ID del usuario.
    """
    try:
        if not pdf.filename.endswith(".pdf"):
            return JSONResponse(content={"error": "El archivo debe ser un PDF."}, status_code=400)

        # Extraer texto del PDF
        text = await process_pdf(pdf.file)
        if not text:
            return JSONResponse(content={"error": "El PDF no contiene texto procesable."}, status_code=400)

        # Crear embeddings para el usuario
        rag_pipeline.create_embeddings(user_id, text)

        return JSONResponse(content={"message": "PDF procesado con éxito."}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/ask/")
async def ask_question(user_id: str = Form(...), question: str = Form(...)):
    """
    Endpoint para hacer preguntas basadas en los PDFs procesados.
    """
    try:
        if not question.strip():
            return JSONResponse(content={"error": "La pregunta no puede estar vacía."}, status_code=400)

        # Consultar el modelo con los embeddings generados
        answer = rag_pipeline.query(user_id, question)
        return JSONResponse(content={"answer": answer}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
