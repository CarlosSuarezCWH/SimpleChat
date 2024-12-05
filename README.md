# PDF Bot

PDF Bot es una aplicación que permite procesar archivos PDF y realizar consultas sobre su contenido utilizando técnicas de RAG (Retrieval-Augmented Generation). Los usuarios pueden cargar archivos PDF, extraer texto, crear embeddings y luego hacer preguntas basadas en el contenido procesado.

## Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/CarlosSuarezCWH/pdf-bot.git
   cd pdf-bot

2. Crea un entorno virtual y actívalo:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa venv\Scripts\activate

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt


**Configuración**

Crea un archivo .env en la raíz del proyecto y agrega la siguiente configuración:

    MODEL_NAME=gpt_neox  # o llama2, bloom según el modelo que desees usar

Si usas un modelo diferente, asegúrate de ajustar el nombre en la variable MODEL_NAME en el archivo .env.

**Uso**
Ejecutar el servidor
Para iniciar el servidor, usa el siguiente comando:

    uvicorn app.main:app --reload

El servidor estará disponible en http://localhost:8000.

**Endpoints**

1. Subir y procesar un archivo PDF

Método: POST
URL: /process-pdf/
Parametros:
pdf: Archivo PDF a cargar.
user_id: ID del usuario.
Ejemplo de solicitud:

    curl -X 'POST' \
    'http://localhost:8000/process-pdf/' \
    -H 'accept: application/json' \
    -H 'Content-Type: multipart/form-data' \
    -F 'pdf=@path_to_pdf_file.pdf' \
    -F 'user_id=123'

2. Realizar una consulta sobre el PDF procesado

Método: POST
URL: /ask/
Parametros:
user_id: ID del usuario.
question: Pregunta que se quiere hacer sobre el contenido del PDF.
Ejemplo de solicitud:

    curl -X 'POST' \
    'http://localhost:8000/ask/' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'user_id=123&question=¿Cuál es el tema principal del documento?'


**Modelos soportados**
El sistema soporta varios modelos de lenguaje como:
GPT-NeoX
Llama 2
Bloom

Para cambiar el modelo, ajusta la variable MODEL_NAME en el archivo .env.

**Contribuciones**
¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar el proyecto, por favor abre un issue o envía un pull request.

**Licencia**
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.



