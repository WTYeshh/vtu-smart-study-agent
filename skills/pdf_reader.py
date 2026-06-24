import os
from typing import List, Dict, Any
from pypdf import PdfReader
from utils.logger import setup_logger

logger = setup_logger("pdf_reader")

class PDFReader:
    """Utility skill to extract and partition text from PDF files (e.g. syllabus/notes)."""

    @staticmethod
    def extract_text(pdf_path: str) -> str:
        """Extracts all text from a given PDF file."""
        if not os.path.exists(pdf_path):
            logger.error(f"PDF file not found at path: {pdf_path}")
            return ""

        try:
            reader = PdfReader(pdf_path)
            full_text = []
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    full_text.append(text)
            logger.info(f"Successfully extracted {len(reader.pages)} pages from {pdf_path}")
            return "\n".join(full_text)
        except Exception as e:
            logger.error(f"Error reading PDF {pdf_path}: {e}")
            return ""

    @staticmethod
    def extract_pages(pdf_path: str) -> List[Dict[str, Any]]:
        """Extracts text page-by-page to keep track of page numbers."""
        pages_content = []
        if not os.path.exists(pdf_path):
            logger.error(f"PDF file not found: {pdf_path}")
            return pages_content

        try:
            reader = PdfReader(pdf_path)
            for idx, page in enumerate(reader.pages):
                text = page.extract_text()
                pages_content.append({
                    "page_number": idx + 1,
                    "text": text or ""
                })
            return pages_content
        except Exception as e:
            logger.error(f"Error reading PDF pages {pdf_path}: {e}")
            return pages_content
