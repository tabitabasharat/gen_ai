import os
from pypdf import PdfReader

def load_pdfs(folder_path):
    docs = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".pdf"):
                path = os.path.join(root, file)
                reader = PdfReader(path)

                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        docs.append(text)

    return docs