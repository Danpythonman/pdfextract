'''
Module for extracting images from a PDF.
'''


from pathlib import Path
from typing import List, Optional

from pdftools.exception import \
    PageNumberOutOfBoundsException, \
    ParentDirectoryDoesNotExistException, \
    PyPDFNotFoundException
from pdftools.utils import generate_unique_filename

try:
    from pypdf import PdfReader
except ModuleNotFoundError as e:
    raise PyPDFNotFoundException()


FILE_DIR = Path(__file__).parent
IMAGE_PDFS_DIR = FILE_DIR / 'image_extract'
IMAGE_PDF_FILE_PATH = IMAGE_PDFS_DIR \
    / 'mvc_chapter_learn_objective_c_for_java_developers.pdf'


def extract_images(
    input_pdf_path: Path,
    pages_to_check: Optional[List[int]] = None,
    output_dir: Optional[Path] = None
):
    '''
    '''

    reader = PdfReader(input_pdf_path)

    if pages_to_check is not None:
        page_list = [page - 1 for page in pages_to_check]
    else:
        page_list = [page for page in reader.pages]

    counter = 0
    reader = PdfReader(IMAGE_PDF_FILE_PATH)
    for page in reader.pages:
        if page in page_list:
            for image in page.images:
                print(f'Extracting {image.name}')
                with open(IMAGE_PDFS_DIR / 'images' / f'{counter}-{image.name}', 'wb') as fp:
                    fp.write(image.data)
                    counter += 1
