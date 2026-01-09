import re

def preprocess_text(text):
    """
    Normaliza el texto extraído del documento para
    dejarlo listo para inferencia con el modelo de lenguaje.
    """

    # Elimina saltos de línea
    text = text.replace("\n", " ")

    # Reemplaza múltiples espacios por uno solo
    text = re.sub(r"\s+", " ", text)

    # Elimina espacios al inicio y al final
    text = text.strip()

    return text
