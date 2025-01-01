from pathlib import Path
from typing import List, Optional
from pdfextract.utils import generate_unique_filename
from pdfextract.exception import \
    PyPDFNotFoundException, \
    ParentDirectoryDoesNotExistException

try:
    from pypdf import PdfReader, PdfWriter
except ModuleNotFoundError as e:
    raise PyPDFNotFoundException()


def extract_pages(
        input_pdf_path: Path,
        pages_to_keep: List[int],
        output_pdf_path: Optional[Path] = None
) -> Path:
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    for i in pages_to_keep:
        p = reader.pages[i]
        writer.add_page(p)

    if not output_pdf_path:
        output_pdf_path = generate_unique_filename()

    if not output_pdf_path.parent.exists():
        raise ParentDirectoryDoesNotExistException(output_pdf_path)

    with open(f'{output_pdf_path}', 'wb') as f:
        writer.write(f)

    return output_pdf_path
