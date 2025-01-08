'''
Module for extracting pages from a PDF.
'''


from pathlib import Path
from typing import List, Optional

from pdftools.exception import \
    PyPDFNotFoundException, \
    ParentDirectoryDoesNotExistException
from pdftools.utils import generate_unique_filename

try:
    from pypdf import PdfReader, PdfWriter, PdfMerger
except ModuleNotFoundError as e:
    raise PyPDFNotFoundException()


def merge_pdfs(
    input_pdf_files: List[Path],
    output_pdf_path: Optional[Path] = None
) -> Path:
    '''
    Merges PDF files and generates a new PDF with merged files.

    :param input_pdf_path: The list of paths of the input PDF files.

    :param output_pdf_path: The path to write the output PDF to.

    :return: The path of the generated PDF.
    '''

    writer = PdfWriter()

    for pdf in input_pdf_files:
        writer.append(pdf)

    if not output_pdf_path:
        output_pdf_path = generate_unique_filename()

    if not output_pdf_path.parent.exists():
        raise ParentDirectoryDoesNotExistException(output_pdf_path)

    with open(f'{output_pdf_path}', 'wb') as f:
        writer.write(f)

    return output_pdf_path
