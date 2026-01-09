from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from config import FORM_ENDPOINT, FORM_KEY

def extract_text_from_pdf(pdf_path):
    client = DocumentAnalysisClient(
        endpoint=FORM_ENDPOINT,
        credential=AzureKeyCredential(FORM_KEY)
    )

    with open(pdf_path, "rb") as f:
        poller = client.begin_analyze_document("prebuilt-document", f)
        result = poller.result()

    text = ""
    for page in result.pages:
        for line in page.lines:
            text += line.content + " "

    return text

