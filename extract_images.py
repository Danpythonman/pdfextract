from pathlib import Path

from pypdf import PdfReader


FILE_DIR = Path(__file__).parent
IMAGE_PDFS_DIR = FILE_DIR / 'image_extract'
IMAGE_PDF_FILE_PATH = IMAGE_PDFS_DIR \
    / 'mvc_chapter_learn_objective_c_for_java_developers.pdf'


def main():
    counter = 0
    reader = PdfReader(IMAGE_PDF_FILE_PATH)
    for page in reader.pages:
        for image in page.images:
            print(f'Extracting {image.name}')
            with open(IMAGE_PDFS_DIR / 'images' / f'{counter}-{image.name}', 'wb') as fp:
                fp.write(image.data)
                counter += 1


if __name__ == '__main__':
    main()
