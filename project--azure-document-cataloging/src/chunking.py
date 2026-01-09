def chunk_text(text, max_length=3000):
    """
    Divide un texto largo en fragmentos de tamaño controlado.
    """

    chunks = []
    start = 0

    while start < len(text):
        end = start + max_length
        chunks.append(text[start:end])
        start = end

    return chunks
