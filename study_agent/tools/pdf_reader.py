"""
PDF Reader Tool.

Reads all Machine Learning syllabus PDFs and
provides their content to AI agents.
"""

from pathlib import Path
from pypdf import PdfReader


def read_syllabus() -> str:
    """
    Reads all PDFs inside data/syllabus
    and returns one combined text.
    """

    syllabus_folder = Path("data/syllabus")

    combined_text = ""

    # Read every PDF in the folder
    for pdf_file in syllabus_folder.glob("*.pdf"):

        reader = PdfReader(pdf_file)

        combined_text += f"\n\n========== {pdf_file.name} ==========\n\n"

        # Read every page
        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                combined_text += page_text + "\n"

    return combined_text