import json
from openai import AzureOpenAI
from config import OPENAI_ENDPOINT, OPENAI_KEY, OPENAI_DEPLOYMENT

# Inicialización del cliente de Azure OpenAI
client = AzureOpenAI(
    api_key=OPENAI_KEY,
    api_version="2024-02-15-preview",
    azure_endpoint=OPENAI_ENDPOINT
)

def classify_text(document_text):
    """
    Clasifica un documento en una categoría definida
    y retorna un JSON con la categoría y su justificación.
    """

    prompt = f"""
Eres un asistente experto en clasificación documental.

Analiza el siguiente texto y clasifícalo en UNA de las siguientes categorías:
- Contrato
- Queja
- Resolución
- Informe
- Comunicación
- Otro

Devuelve únicamente un JSON con esta estructura:
{{
  "categoria": "<categoria>",
  "justificacion": "<explicacion breve basada en el contenido>"
}}

Texto del documento:
{document_text}
"""

    response = client.chat.completions.create(
        model=OPENAI_DEPLOYMENT,
        messages=[
            {"role": "system", "content": "Eres un clasificador documental profesional."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return {
            "categoria": "Otro",
            "justificacion": "No fue posible interpretar la respuesta del modelo."
        }

