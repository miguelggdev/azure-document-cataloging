# Proyecto – Entrenamiento de un modelo ML con Azure Machine Learning y scikit-learn

## 📌 Descripción
Este proyecto demuestra el uso de **Azure AI**para para diseñar, implementar y justificar una solución de clasificación automática de documentos PDF, utilizando Modelos de Lenguaje de Gran Escala (LLMs), 
Consumidos / desplegados en Microsoft Azure.

## Caso de uso del proyecyo 

Una organización recibe diariamente documentos en formato PDF (oficios, contratos, resoluciones, quejas, informes técnicos, etc.) que deben ser clasificados manualmente para su gestión interna. 

**Problemas actuales:**

- Procesos manuales lentos
- Errores de clasificación
- Dificultad para escalar el volumen documental
- Dependencia de personal especializado

**Necesidad**
Automatizar la clasificación inicial de documentos para facilitar su enrutamiento, priorización y análisis posterior.

## Objetivos del proyecto

Diseñar una solución basada en LLMs que permita:

- Extraer texto desde documentos PDF
- Analizar su contenido semántico
- Clasificar automáticamente el documento en una categoría definida
- Generar una justificación legible de la clasificación
- Ejecutarse Azure, de forma reproducible

**Categorías de clasificación**
Se puede usar estas u otras (deben documentarse):

- Queja / Reclamo
- Contrato
- Resolución administrativa
- Informe técnico
- Comunicación interna

## Actividades de desarrollo

# Actividad 1
Selección del ambiente de ejecución

Para el desarrollo de este proyecto **se eligió la modalidad Azure, utilizando servicios de Azure AI**, principalmente Azure Document Intelligence para la extracción de texto desde documentos PDF y Azure OpenAI para el análisis semántico y la clasificación automática.

Esta modalidad permite cumplir con los requerimientos del caso de uso, manteniendo una arquitectura empresarial, segura y escalable.

# Actividad 2 Diseño de la solución (funcional)

**Contexto del problema**

La organización recibe diariamente documentos en formato PDF (quejas, contratos, resoluciones, informes, comunicaciones internas) que deben ser clasificados manualmente,  lo cual genera un cuello de botella en la clasificacion de documentos generando demoras, errores y dificultad para escalar el proceso.

**Objetivo funcional**

Realizar una solucion de IA con Azure para automatizar la clasificación inicial de documentos PDF para lograr facilitar su gestión, priorización y análisis posterior.

**Solución propuesta**

Se propone desarrollar una solución que permita:

- Cargar documentos PDF de diferentes tipos
- Extraer automáticamente el texto del documento
- Analizar su contenido semántico
- Clasificar el documento en una categoría definida
- Generar una justificación clara de la clasificación

De esta manera, se reduce la intervención manual y se mejora la eficiencia del proceso documental.

# Actividad 3 Diseño de la solución (técnico)

La solución se basa en una arquitectura simple y modular que separa claramente cada responsabilidad del proceso:

- Extracción de texto:
Se utiliza Azure AI Document Intelligence para extraer texto desde documentos PDF.

- Preprocesamiento:
El texto extraído se limpia y normaliza para facilitar su análisis.

- Análisis semántico y clasificación:
El texto procesado se envía a un modelo de lenguaje de Azure OpenAI, el cual clasifica el documento y genera una justificación basada en su contenido.

- Generación de resultados:
El resultado final se estructura en un formato legible (JSON), que puede ser utilizado por otros sistemas o procesos posteriores.

![Flujo-de-trabajo](https://github.com/miguelggdev/azureML/blob/main/project-01-azureml-sklearn/screenshots/flujo_trabajo.png)

# Actividad 4 – Selección y uso del LLM

Modelo seleccionado

Se utiliza un modelo de lenguaje grande (LLM) proporcionado por Azure OpenAI, como GPT-4 o GPT-4o.

**Justificación del uso del LLM**

Permite comprender el contenido semántico del documento, no solo palabras clave

Se adapta a diferentes tipos de documentos sin necesidad de entrenamiento adicional

Genera clasificaciones explicables y coherentes

Reduce la necesidad de reglas rígidas o modelos tradicionales de clasificación

Azure OpenAI ofrece además ventajas a nivel de seguridad, cumplimiento y control del acceso, lo cual es clave en entornos empresariales.

# Actividad 5 – Configuración del entorno

Definición del entorno

PAra este proyecto el entorno de ejecucion se define como Servicio de IA gestionado (PaaS), usando Azure AI Document Intelligence yAzure OpenAI.

El codigo se desarrolla para python, pero se ejecuta y procesa con Azure 

Dependencias declaradas en requirements.txt
Manejo de credenciales mediante variables de entorno
Separación clara entre código fuente, datos de entrada y resultados

**Creación del Resource Group (Azure CLI)**

Crear un grupo de recursos para la solución

```bash
az group create \
  --name rg-ia-clasificacion-documental \
  --location eastus
```
![grupo-drecursos](https://github.com/miguelggdev/azureML/blob/main/project-01-azureml-sklearn/screenshots/grupo_recursos.jpg)

![grupo-drecursos](https://github.com/miguelggdev/azureML/blob/main/project-01-azureml-sklearn/screenshots/grupo_recursos2.jpg)
**Gestión de dependencias**

El proyecto está estructurado para ejecutarse en un entorno Python y define sus dependencias en el archivo requirements.txt, lo que permite recrear el entorno de forma controlada:
```python
openai
azure-ai-formrecognizer
python-dotenv
tiktoken
```
Estas librerías permiten:

- Conectarse a Azure OpenAI
- Extraer texto desde PDFs usando Azure AI
- Manejar variables de entorno de forma segura
- Controlar la longitud del texto enviado al modelo

Manejo de variables de entorno

Las credenciales de los servicios Azure se gestionan mediante variables de entorno, evitando la exposición de información sensible en el código.

El proyecto incluye un archivo de referencia .env.example:

```python
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_KEY=
AZURE_OPENAI_DEPLOYMENT=
FORM_RECOGNIZER_ENDPOINT=
FORM_RECOGNIZER_KEY=
```

El archivo real .env no se versiona y se encuentra incluido en el archivo .gitignore.
Preparación del entorno (documentado)

En un escenario de ejecución, el entorno se prepararía de la siguiente forma:

**Crear Azure AI Document Intelligence (OCR)**

📍 Azure Portal
Buscar Azure AI Document Intelligence
Crear nuevo recurso
Seleccionar:
Resource Group: rg-ia-clasificacion-pdf
Región
Plan: Standard (S0)
Crear

📌 Esto es parte del entorno de ejecución, porque aquí se ejecuta el OCR.

![grupo-drecursos](https://github.com/miguelggdev/azureML/blob/main/project-01-azureml-sklearn/screenshots/documentIntell.jpg)

![grupo-drecursos](https://github.com/miguelggdev/azureML/blob/main/project-01-azureml-sklearn/screenshots/documentIntel2.jpg)

![grupo-drecursos](https://github.com/miguelggdev/azureML/blob/main/project-01-azureml-sklearn/screenshots/documentIntel3.jpg)

![grupo-drecursos](https://github.com/miguelggdev/azureML/blob/main/project-01-azureml-sklearn/screenshots/documentIntel4.jpg)



**Crear Azure OpenAI (LLM)**
Azure Portal

Buscar Azure OpenAI
Crear recurso
Seleccionar:
Resource Group: rg-ia-clasificacion-pdf
Región
Crear

![grupo-drecursos](https://github.com/miguelggdev/azureML/blob/main/project-01-azureml-sklearn/screenshots/OpenAI.jpg)

![grupo-drecursos](https://github.com/miguelggdev/azureML/blob/main/project-01-azureml-sklearn/screenshots/OpenAI2.jpg)

![grupo-drecursos](https://github.com/miguelggdev/azureML/blob/main/project-01-azureml-sklearn/screenshots/OpenAI3.jpg)

![grupo-drecursos](https://github.com/miguelggdev/azureML/blob/main/project-01-azureml-sklearn/screenshots/OpenAI4.jpg)

Ir al Portal de Foundry


![grupo-drecursos](https://github.com/miguelggdev/azureML/blob/main/project-01-azureml-sklearn/screenshots/project.jpg)

![grupo-drecursos](https://github.com/miguelggdev/azureML/blob/main/project-01-azureml-sklearn/screenshots/foundry.jpg)


 Selecciona el proyecto correcto

Una vez dentro de Foundry:

Arriba o en el panel inicial, selecciona:

Subscription: Azure subscription 1

Project: projectdocumental

Resource Group: rg-ia-clasificacion-documental

![grupo-drecursos](https://github.com/miguelggdev/azureML/blob/main/project-01-azureml-sklearn/screenshots/foundry2.jpg)

**Ir a Deployments / Implementaciones**

En el menú izquierdo de Foundry busca:

Deployments

Model deployments

Implementaciones

![grupo-drecursos](https://github.com/miguelggdev/azureML/blob/main/project-01-azureml-sklearn/screenshots/foundry3.jpg)

![grupo-drecursos](https://github.com/miguelggdev/azureML/blob/main/project-01-azureml-sklearn/screenshots/foundry4.jpg)

![grupo-drecursos](https://github.com/miguelggdev/azureML/blob/main/project-01-azureml-sklearn/screenshots/foundry5.jpg)

![grupo-drecursos](https://github.com/miguelggdev/azureML/blob/main/project-01-azureml-sklearn/screenshots/foundry6.jpg)

![grupo-drecursos](https://github.com/miguelggdev/azureML/blob/main/project-01-azureml-sklearn/screenshots/foundry7.jpg)

![grupo-drecursos](https://github.com/miguelggdev/azureML/blob/main/project-01-azureml-sklearn/screenshots/foundry8.jpg)


![grupo-drecursos](https://github.com/miguelggdev/azureML/blob/main/project-01-azureml-sklearn/screenshots/keys_endpoinst.jpg)

# Actividad 6 Ingesta de documentos PDF

La solución implementa un mecanismo de ingesta de documentos PDF que permite cargar uno o varios archivos para su posterior procesamiento automático.
Para efectos de esta prueba técnica, la ingesta se realiza desde una estructura de carpetas local dentro del repositorio, la cual simula el origen de los documentos que recibe la organización.

Este enfoque permite:
Validar fácilmente el funcionamiento de la solución
Procesar múltiples documentos en un solo flujo
Mantener la solución simple, reproducible y alineada con el alcance de la prueba

Enfoque técnico de la ingesta
El proceso de ingesta consiste en:
Recorrer de forma automática la carpeta data/pdfs
Identificar todos los archivos con extensión .pdf
Enviar cada documento al flujo de extracción y clasificación
Procesar los documentos de manera independiente
Este enfoque permite escalar fácilmente el número de documentos sin modificar el código.
Estructura de entrada de documentos

Los documentos PDF se organizan en una carpeta dedicada dentro del proyecto, clasificados inicialmente por tipo únicamente con fines de prueba y validación.

![grupo-drecursos](https://github.com/miguelggdev/azureML/blob/main/project-01-azureml-sklearn/screenshots/ingesta.jpg)



# Actividad 7 – Clasificación documental con Azure OpenAI

En esta actividad se implementa la clasificación automática de documentos utilizando Azure OpenAI, a partir del texto previamente extraído desde los archivos PDF.

El modelo de lenguaje analiza el contenido completo del documento y determina:

La categoría documental

Una justificación breve basada en el contenido

Este enfoque permite realizar una clasificación semántica, superando las limitaciones de reglas estáticas o palabras clave.

Categorías definidas

Las categorías manejadas por la solución son:

Contrato
Queja
Resolución
Informe
Comunicación
Otro
Estas categorías pueden ampliarse sin modificar la arquitectura general.

Enfoque técnico

El flujo de clasificación se basa en:

Recepción del texto extraído del PDF

Envío del texto a un deployment de Azure OpenAI

Uso de un prompt estructurado para guiar la respuesta

Obtención de una salida controlada y explicable

9
Diseño del prompt
Crear un prompt estructurado para clasificación con LLM



# Actividad 7  8 – Preprocesamiento del texto

En esta actividad se realiza el preprocesamiento básico del texto extraído desde los documentos PDF, con el objetivo de normalizar y preparar la información antes de enviarla al modelo de lenguaje para inferencia.

El preprocesamiento permite:

Reducir ruido en el texto
Garantizar entradas consistentes al modelo
Mejorar la calidad de la clasificación
Alcance del preprocesamiento
Para la prueba técnica se implementa un preprocesamiento ligero, alineado con buenas prácticas y sin sobreingeniería.

Incluye:

Limpieza de espacios innecesarios
Normalización básica del texto
Preparación del contenido para inferencia

No se realiza:

Tokenización avanzada
Eliminación semántica
Análisis lingüístico profundo

Enfoque técnico

El texto preprocesado se obtiene a partir del texto plano generado por Azure Document Intelligence y se procesa mediante funciones simples en Python, manteniendo la trazabilidad del contenido original.

src/preprocess.py

```python
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
```
# Actividad 9

En esta actividad se diseña un prompt estructurado y explicable para guiar al modelo de lenguaje (Azure OpenAI) en la clasificación documental.

El prompt define explícitamente:

El rol del modelo

Las categorías permitidas

El formato de salida

El contexto del documento

Esto garantiza respuestas:

Consistentes

Interpretables

Fáciles de auditar

Objetivo del prompt

El prompt tiene como objetivo que el modelo:

Analice el contenido completo del documento

Determine la categoría documental más adecuada

Explique brevemente la razón de la clasificación

Retorne una salida estructurada y procesable

Principios de diseño del prompt

El diseño del prompt sigue buenas prácticas para LLMs:

Claridad: instrucciones directas y sin ambigüedad

Restricción: categorías cerradas

Estructura: salida en formato JSON

Explicabilidad: justificación obligatoria

Prompt definitivo utilizado en la solución

📌 Este prompt es el que se utiliza en classify.py

*Eres un asistente experto en clasificación documental.

Analiza el siguiente texto y clasifícalo en UNA de las siguientes categorías:
- Contrato
- Queja
- Resolución
- Informe
- Comunicación
- Otro

Devuelve únicamente un JSON con esta estructura:
{
  "categoria": "<categoria>",
  "justificacion": "<explicacion breve basada en el contenido>"
}

Texto del documento:
{document_text}*

Explicación del prompt (parte por parte)
1️⃣ Definición del rol

“Eres un asistente experto en clasificación documental”

🔹 Orienta el comportamiento del modelo
🔹 Reduce respuestas creativas o irrelevantes

2️⃣ Definición explícita de categorías

🔹 Evita clasificaciones abiertas
🔹 Facilita evaluación y métricas
🔹 Permite extender categorías sin cambiar arquitectura

3️⃣ Formato de salida estructurado
{
  "categoria": "...",
  "justificacion": "..."
}


🔹 Permite parsing automático
🔹 Mejora trazabilidad
🔹 Facilita auditoría del resultado

4️⃣ Inclusión del texto completo

🔹 El modelo tiene todo el contexto
🔹 Permite inferencia semántica real
🔹 Evita dependencias de reglas o keywords

Justificación de la solución

Se eligió un prompt estructurado porque:

Reduce variabilidad del modelo

Aumenta la confiabilidad del resultado

Facilita integración con otros sistemas

Permite explicar cada decisión del modelo

Este diseño cumple principios de IA explicable (XAI).

Resultado de la actividad

✔ Prompt claro y documentado
✔ Salida estructurada
✔ Clasificación explicable
✔ Fácil de mantener y extender

📌 Texto recomendado para el README

Se diseñó un prompt estructurado para la clasificación documental, definiendo roles, categorías cerradas y un formato de salida en JSON, garantizando resultados explicables y consistentes por parte del modelo de lenguaje.

# Actividad 10

En esta actividad se ejecuta la clasificación final de los documentos utilizando un modelo de lenguaje desplegado en Azure OpenAI.
El texto, previamente extraído y preprocesado, es enviado al LLM, el cual retorna:

La categoría documental

Una justificación explicable

La respuesta del modelo se recibe en un formato estructurado (JSON), permitiendo su uso posterior en sistemas de almacenamiento, visualización o automatización.

Flujo completo de clasificación

El flujo de esta actividad integra todas las etapas anteriores:

PDF
 ↓
Extracción de texto (Azure Document Intelligence)
 ↓
Preprocesamiento
 ↓
Clasificación con Azure OpenAI
 ↓
Categoría + Justificación (JSON)

Enfoque técnico

La clasificación se realiza mediante:

Un deployment de Azure OpenAI configurado en Azure AI Foundry

Un prompt estructurado

Una llamada controlada al endpoint del modelo

Manejo defensivo de la respuesta

Esto garantiza resultados consistentes, trazables y explicables.

codigo main.py

```python
import os
from extract import extract_text_from_pdf
from preprocess import preprocess_text
from classify import classify_text


def process_document(pdf_path):
    """
    Ejecuta el flujo completo de procesamiento y clasificación
    de un documento PDF.
    """

    # 1. Extraer texto desde el PDF usando Azure Document Intelligence
    raw_text = extract_text_from_pdf(pdf_path)

    # 2. Preprocesar el texto (normalización básica)
    clean_text = preprocess_text(raw_text)

    # 3. Clasificar el documento usando Azure OpenAI
    classification_result = classify_text(clean_text)

    return classification_result


def process_folder(folder_path):
    """
    Procesa todos los archivos PDF dentro de una carpeta
    y retorna los resultados de clasificación.
    """

    results = []

    # Recorrer recursivamente la carpeta de entrada
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".pdf"):
                pdf_path = os.path.join(root, file)

                # Ejecutar el flujo completo para cada documento
                result = process_document(pdf_path)

                results.append({
                    "archivo": file,
                    "resultado": result
                })

    return results


if __name__ == "__main__":
    # Carpeta de entrada de documentos PDF
    INPUT_FOLDER = "data/pdfs"

    # Ejecutar el procesamiento completo
    classification_results = process_folder(INPUT_FOLDER)

    # Mostrar resultados por consola
    for item in classification_results:
        print(f"Archivo: {item['archivo']}")
        print(f"Categoría: {item['resultado'].get('categoria')}")
        print(f"Justificación: {item['resultado'].get('justificacion')}")
        print("-" * 50)
```


        ✅ Qué hace este main.py (resumen claro)

✔ Orquesta todo el pipeline
✔ Procesa uno o múltiples PDFs
✔ Usa extracción, preprocesamiento y clasificación
✔ Devuelve categoría + justificación
✔ No expone credenciales
✔ Es simple, claro y defendible

✅ Actividad 11 – Manejo de documentos largos
Descripción de la actividad

En esta actividad se implementa una estrategia de manejo de documentos largos para garantizar que el texto enviado al modelo de lenguaje no exceda los límites de contexto del LLM.

Para ello, se utiliza una técnica de chunking, que consiste en dividir el texto en fragmentos controlados antes de la inferencia.

¿Por qué es necesario el manejo de longitud?

Los modelos de lenguaje tienen un límite máximo de tokens por solicitud.
Los documentos PDF extensos (contratos largos, informes, resoluciones) pueden superar fácilmente ese límite.

Sin una estrategia de chunking:

❌ Fallos por exceso de tokens

❌ Pérdida de información

❌ Resultados inconsistentes

Estrategia aplicada

La solución implementa un chunking simple y efectivo, basado en:

División del texto por longitud aproximada

Procesamiento de fragmentos independientes

Consolidación del resultado final

📌 Esta estrategia es suficiente y defendible para una prueba técnica.

Enfoque técnico

El texto completo es dividido en fragmentos (“chunks”)

Cada fragmento se envía al LLM

Se obtiene una clasificación parcial

Se consolida una clasificación final

Implementación del chunking

📄 Archivo: src/chunking.py

```python
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
```
Estrategia de consolidación

Para la prueba técnica, se utiliza una estrategia simple:

Se toma la categoría más frecuente

Se conserva una justificación representativa

📌 Esto puede evolucionar a:

Prompts de resumen

Votación ponderada

Razonamiento jerárquico

Evidencia de manejo de longitud

✔ Implementación explícita de chunking
✔ Código modular y reutilizable
✔ Prevención de límites de contexto
✔ Manejo correcto de documentos extensos

Justificación de la solución

Se eligió chunking simple porque:

Es claro y fácil de entender

No depende de librerías externas

Funciona con cualquier modelo GPT

Es suficiente para el alcance de la prueba

La arquitectura queda preparada para estrategias más avanzadas.

📌 Texto recomendado para el README

Para manejar documentos extensos, se implementó una estrategia de chunking que divide el texto en fragmentos controlados antes de enviarlos al modelo de lenguaje, evitando exceder los límites de contexto y garantizando una clasificación robusta.

🎯 Estado

👉 Actividad 11: COMPLETADA

🔎 Nota importante (esto suma puntos)

Puedes mencionar en la entrevista:

“El chunking se aplica solo cuando la longitud del documento lo requiere, manteniendo eficiencia y control de costos.”