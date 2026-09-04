from pathlib import Path
from pypdf import PdfReader


def extract_pdf_text(pdf_path: str, start_page: int, end_page: int):
    """Extract text from all pages of a PDF and return it as one string."""
    reader = PdfReader(pdf_path)

    pages = []

    for page in reader.pages[start_page:end_page]:
        text = page.extract_text()

        if text:
            pages.append(text)

    return "\n".join(pages)