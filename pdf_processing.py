import pdfplumber
from typing import BinaryIO, Optional
import re

def clean_text(text: str) -> str:
    """
    Limpia el texto eliminando caracteres especiales y espacios innecesarios.
    """
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    return text

async def process_pdf(file: BinaryIO) -> Optional[str]:
    """
    Extrae texto del PDF y lo limpia.
    """
    try:
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

        text = clean_text(text)
        return text if text else None
    except Exception as e:
        print(f"Error procesando el PDF: {e}")
        return None
