import os
from extract import extract_text_from_pdf
from preprocess import preprocess_text
from classify import classify_text
from chunking import chunk_text
from collections import Counter


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


def process_folder(folder_path):
    """
    Procesa todos los archivos PDF dentro de una carpeta
    y retorna los resultados de clasificación.
    """

    results = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".pdf"):
                pdf_path = os.path.join(root, file)

                result = process_document(pdf_path)

                results.append({
                    "archivo": file,
                    "resultado": result
                })

    return results


if __name__ == "__main__":
    # Carpeta de entrada de documentos
    INPUT_FOLDER = "data/pdfs"

    # Ejecutar el procesamiento completo
    classification_results = process_folder(INPUT_FOLDER)

    # Mostrar resultados por consola
    for item in classification_results:
        print(f"Archivo: {item['archivo']}")
        print(f"Categoría: {item['resultado']['categoria']}")
        print(f"Justificación: {item['resultado']['justificacion']}")
        print("-" * 50)