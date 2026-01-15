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

# Actividad 1 Selección del ambiente de ejecución

Para el desarrollo de este proyecto **se eligió la modalidad Azure, utilizando servicios de Azure AI**, principalmente Azure Document Intelligence para la extracción de texto desde documentos PDF y Azure OpenAI para el análisis semántico y la clasificación automática.

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

Se opta por una arquitectura basada en eventos y serverless, donde la carga de documentos desencadena automáticamente el procesamiento y clasificación.

![arquitectura](https://github.com/miguelggdev/azure-document-cataloging/blob/main/project--azure-document-cataloging/screenshots/arquitectura.png)

**- Ingesta de documentos:**
Se cargan documentos en un Blob desde la consola de Azure o CLI

**- Extracción de texto:**
Se utiliza Azure AI Document Intelligence para extraer texto desde documentos PDF.

**- Preprocesamiento:**
El texto extraído se limpia y normaliza para facilitar su análisis.

**- Análisis semántico y clasificación:**
El texto procesado se envía a un modelo de lenguaje de Azure OpenAI, el cual clasifica el documento y genera una justificación basada en su contenido.

**- Generación de resultados:**
El resultado final se estructura en un formato legible (JSON), que puede ser utilizado por otros sistemas o procesos posteriores.

![Flujo-de-trabajo](https://github.com/miguelggdev/azure-document-cataloging/blob/main/project--azure-document-cataloging/screenshots/flujo_trabajo.png)

# Actividad 4 – Selección y uso del LLM

**Modelo seleccionado**

Se utiliza un modelo de lenguaje grande (LLM) proporcionado por Azure OpenAI, como GPT-4

**Justificación del uso del LLM**

- Permite comprender el contenido semántico del documento.
- Se adapta a diferentes tipos de documentos sin necesidad de entrenamiento adicional.
- Genera clasificaciones explicables y coherentes.


# Actividad 5 – Configuración del entorno

**Definición del entorno**

Para este proyecto el entorno de ejecucion se define como Servicio de IA gestionado (PaaS), usando Azure AI Document Intelligence yAzure OpenAI. 
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
![grupo-drecursos](https://github.com/miguelggdev/azure-document-cataloging/blob/main/project--azure-document-cataloging/screenshots/grupo_recursos.jpg)

![grupo-drecursos](https://github.com/miguelggdev/azure-document-cataloging/blob/main/project--azure-document-cataloging/screenshots/grupo_recursos2.jpg)

**Creación Almacenamiento de datos Azure Blob Storage**
![contenedores](https://github.com/miguelggdev/azure-document-cataloging/blob/main/project--azure-document-cataloging/screenshots/contenedor.jpg)

![contenedores](https://github.com/miguelggdev/azure-document-cataloging/blob/main/project--azure-document-cataloging/screenshots/contenedores_creados.jpg)

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
**Crear Azure AI Document Intelligence (OCR)**

Azure Portal:
Buscar Azure AI Document Intelligence
Crear nuevo recurso
Seleccionar:
Resource Group: rg-ia-clasificacion-pdf
Región
Plan: Standard (S0)
Crear

![grupo-drecursos](https://github.com/miguelggdev/azure-document-cataloging/blob/main/project--azure-document-cataloging/screenshots/documentIntell.jpg)

**Crear Azure OpenAI (LLM)**
Azure Portal:
Buscar Azure OpenAI
Crear recurso
Seleccionar:
Resource Group: rg-ia-clasificacion-pdf
Región
Crear

![grupo-drecursos](https://github.com/miguelggdev/azure-document-cataloging/blob/main/project--azure-document-cataloging/screenshots/OpenAI.jpg)

![grupo-drecursos](https://github.com/miguelggdev/azure-document-cataloging/blob/main/project--azure-document-cataloging/screenshots/OpenAI2.jpg)

![grupo-drecursos](https://github.com/miguelggdev/azure-document-cataloging/blob/main/project--azure-document-cataloging/screenshots/OpenAI3.jpg)

![grupo-drecursos](https://github.com/miguelggdev/azure-document-cataloging/blob/main/project--azure-document-cataloging/screenshots/OpenAI4.jpg)

Ir al Portal de Foundry

![grupo-drecursos](https://github.com/miguelggdev/azure-document-cataloging/blob/main/project--azure-document-cataloging/screenshots/project.jpg)

![grupo-drecursos](https://github.com/miguelggdev/azure-document-cataloging/blob/main/project--azure-document-cataloging/screenshots/foundry.jpg)


 Seleccionar el proyecto correcto
 y verificar:

Subscription: Azure subscription 1
Project: projectdocumental
Resource Group: rg-ia-clasificacion-documental

![grupo-drecursos](https://github.com/miguelggdev/azure-document-cataloging/blob/main/project--azure-document-cataloging/screenshots/foundry2.jpg)

**Ir a Deployments / Implementaciones**

![grupo-drecursos](https://github.com/miguelggdev/azure-document-cataloging/blob/main/project--azure-document-cataloging/screenshots/foundry3.jpg)

![grupo-drecursos](https://github.com/miguelggdev/azure-document-cataloging/blob/main/project--azure-document-cataloging/screenshots/foundry4.jpg)

![grupo-drecursos](https://github.com/miguelggdev/azure-document-cataloging/blob/main/project--azure-document-cataloging/screenshots/foundry5.jpg)

![grupo-drecursos](https://github.com/miguelggdev/azure-document-cataloging/blob/main/project--azure-document-cataloging/screenshots/foundry6.jpg)

![grupo-drecursos](https://github.com/miguelggdev/azure-document-cataloging/blob/main/project--azure-document-cataloging/screenshots/foundry7.jpg)

![grupo-drecursos](https://github.com/miguelggdev/azureML/blob/main/project-01-azureml-sklearn/screenshots/foundry8.jpg)


![grupo-drecursos](https://github.com/miguelggdev/azure-document-cataloging/blob/main/project--azure-document-cataloging/screenshots//keys_endpoinst.jpg)

# Actividad 6 Ingesta de documentos PDF

Para el proyecto se propone realizar la ingesta de documentos en un Blob Storage para centralizar la carga de documentos PDF y habilitar el procesamiento automático por eventos.

Se utiliza Azure Blob Storage como repositorio de entrada.

Se crea un contenedor llamado input-pdfs.
Los documentos PDF son cargados manualmente o vía CLI.
Cada carga de archivo genera un evento de almacenamiento.

contenedor
![contenedor](https://github.com/miguelggdev/azure-document-cataloging/blob/main/project--azure-document-cataloging/screenshots/contenedor.jpg)

![contenedor](https://github.com/miguelggdev/azure-document-cataloging/blob/main/project--azure-document-cataloging/screenshots/contenedores_creados.jpg)


# Actividad 6 – Clasificación documental con Azure OpenAI

Se implementa la clasificación automática de documentos utilizando Azure OpenAI, a partir del texto previamente extraído desde los archivos PDF.

El modelo de lenguaje analiza el contenido completo del documento y determina:

- La categoría documental
- Una justificación breve basada en el contenido
- Realizar la clasificación semántica
- Categorías definidas

Las categorías manejadas por la solución son:

- Contrato
- Queja
- Resolución
- Informe
- Comunicación
- Otro


**Enfoque técnico**

El flujo de clasificación se basa en:

- Carga del archivo al Blob
- Recepción del texto extraído del PDF
- Envío del texto a un deployment de Azure OpenAI
- Uso de un prompt estructurado para guiar la respuesta
- Json de Salida

# Actividad 7 - Extraccion del texto

El documento PDF subido al Blob se transforma en texto estructurado para ser entregado el LLM

FLUJO PASO A PASO DE LA EXTRACCIÓN
- Se detecta el archivo PDF se sube a Blob Storage y se dispara la Azure Function (Blob Trigger)
- Se envía el PDF a Document Intelligence, el archivo se abre en binario y se envía al endpoint del servicio
- Azure analiza el documento  y realiza el reconocimiento de texto
- Se recupera el resultado, Azure devuelve un objeto estructurado, se recorren páginas → líneas
- Se concatena el texto y queda listo para procesar por el LLM

# Actividad 8 – Preprocesamiento del texto

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


# Actividad 8 

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

En esta actividad se diseña un prompt estructurado para guiar al modelo de lenguaje (Azure OpenAI) en la clasificación documental, definiendo roles, categorías cerradas y un formato de salida en JSON.

El prompt define explícitamente:

- El rol del modelo
- Las categorías permitidas
- El formato de salida
- El contexto del documento

Objetivo del prompt

El prompt tiene como objetivo que el modelo:

Analice el contenido completo del documento

Determine la categoría documental más adecuada

Explique brevemente la razón de la clasificación

Retorne una salida estructurada y procesable

Principios de diseño del prompt

El diseño del prompt sigue buenas prácticas para LLMs:

- Claridad: instrucciones directas y sin ambigüedad
- Restricción: categorías cerradas
- Estructura: salida en formato JSON

**Prompt definitivo utilizado en la solución**

 Este prompt es el que se utiliza en classify.py
```python
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
```


Justificación de la solución

Se eligió un prompt estructurado porque:

- Reduce variabilidad del modelo
- Aumenta la confiabilidad del resultado
- Facilita integración con otros sistemas
- Permite explicar cada decisión del modelo

**Resultado de la actividad**

✔ Prompt claro y documentado
✔ Salida estructurada
✔ Clasificación explicable
✔ Fácil de mantener y extender


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

✔ Orquesta todo el pipeline
✔ Procesa uno o múltiples PDFs
✔ Usa extracción, preprocesamiento y clasificación
✔ Devuelve categoría + justificación
✔ No expone credenciales
✔ Es simple, claro y defendible

# Actividad 11 – Manejo de documentos largos

En esta actividad se implementa una estrategia de manejo de documentos largos para garantizar que el texto enviado al modelo de lenguaje no exceda los límites de contexto del LLM.

Se utiliza una técnica de chunking, que consiste en dividir el texto en fragmentos controlados antes de la inferencia.

Los modelos de lenguaje tienen un límite máximo de tokens por solicitud.
Los documentos PDF extensos (contratos largos, informes, resoluciones) pueden superar fácilmente ese límite.

**Estrategia aplicada**

La solución implementa un chunking simple y efectivo, basado en:

División del texto por longitud aproximada
Procesamiento de fragmentos independientes
Consolidación del resultado final


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

Para manejar documentos extensos, se implementó una estrategia de chunking que divide el texto en fragmentos controlados antes de enviarlos al modelo de lenguaje, evitando exceder los límites de contexto y garantizando una clasificación robusta.
