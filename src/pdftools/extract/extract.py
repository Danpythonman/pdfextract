'''
Module for extracting pages from a PDF.
'''


from pathlib import Path
from typing import List, Optional

from pdftools.exception import \
    PageNumberOutOfBoundsException, \
    ParentDirectoryDoesNotExistException, \
    PyPDFNotFoundException
from pdftools.utils import generate_unique_filename

try:
    from pypdf import PdfReader, PdfWriter
except ModuleNotFoundError as e:
    raise PyPDFNotFoundException()


def extract_pages(
        input_pdf_path: Path,
        pages_to_keep: List[int],
        output_pdf_path: Optional[Path] = None
) -> Path:
    '''
    Extracts pages from a PDF and generates a new PDF with just the extracted
    pages.

    :param input_pdf_path: The path of the input PDF file.

    :param pages_to_keep: A list of page numbers to extract from the input PDF.

    :param output_pdf_path: The path to write the output PDF to.

    :return: The path of the generated PDF.
    '''

    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    for i in pages_to_keep:
        if i-1 >= len(reader.pages):
            raise PageNumberOutOfBoundsException(input_pdf_path, i)
        p = reader.pages[i-1]
        writer.add_page(p)

    if not output_pdf_path:
        output_pdf_path = generate_unique_filename()

    if not output_pdf_path.parent.exists():
        raise ParentDirectoryDoesNotExistException(output_pdf_path)

    with open(f'{output_pdf_path}', 'wb') as f:
        writer.write(f)

    return output_pdf_path
