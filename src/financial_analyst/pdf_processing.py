from pathlib import Path
from pypdf import PdfReader


def extract_pdf_text(pdf_path: str):
    """Extract text from all pages of a PDF and return it as one string."""
    reader = PdfReader(pdf_path)

    pages = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            pages.append(text)

    return "\n".join(pages)