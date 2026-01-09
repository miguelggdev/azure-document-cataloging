import azure.functions as func
import logging
import tempfile
import os
from ..src.extract import extract_text_from_pdf
from ..src.preprocess import preprocess_text
from ..src.classify import classify_text
from ..src.chunking import chunk_text
from collections import Counter

app = func.FunctionApp()

def process_document(pdf_path):
    """
    Ejecuta el flujo completo de procesamiento y clasificación
    de un documento PDF, incluyendo manejo de documentos largos.
    """

    # 1. Extracción de texto desde el PDF
    raw_text = extract_text_from_pdf(pdf_path)

    # 2. Preprocesamiento del texto
    clean_text = preprocess_text(raw_text)

    # 3. División del texto en chunks para manejar documentos largos
    chunks = chunk_text(clean_text)

    # 4. Clasificación de cada fragmento
    chunk_results = []
    for chunk in chunks:
        result = classify_text(chunk)
        chunk_results.append(result)

    # 5. Consolidación de resultados (votación simple por categoría)
    categories = [res["categoria"] for res in chunk_results]
    most_common_category = Counter(categories).most_common(1)[0][0]

    # Se selecciona una justificación representativa
    justification = next(
        res["justificacion"]
        for res in chunk_results
        if res["categoria"] == most_common_category
    )

    return {
        "categoria": most_common_category,
        "justificacion": justification
    }

@app.blob_trigger(arg_name="myblob", path="pdfs/{name}", connection="AzureWebJobsStorage")
def process_blob(myblob: func.InputStream):
    logging.info(f"Processing blob: {myblob.name}")

    # Guardar el blob en un archivo temporal
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
        temp_file.write(myblob.read())
        temp_path = temp_file.name

    try:
        # Procesar el documento
        result = process_document(temp_path)
        logging.info(f"Classification result: {result}")
    except Exception as e:
        logging.error(f"Error processing blob {myblob.name}: {str(e)}")
    finally:
        # Limpiar el archivo temporal
        os.unlink(temp_path)