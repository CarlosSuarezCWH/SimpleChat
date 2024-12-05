from app.models.gpt_neox import GPTNeoXModel
from app.models.llama2 import Llama2Model
from app.models.bloom import BloomModel
from app.config import MODEL_NAME

def load_model():
    if MODEL_NAME == "gpt_neox":
        return GPTNeoXModel()
    elif MODEL_NAME == "llama2":
        return Llama2Model()
    elif MODEL_NAME == "bloom":
        return BloomModel()
    else:
        raise ValueError(f"Modelo no soportado: {MODEL_NAME}")
