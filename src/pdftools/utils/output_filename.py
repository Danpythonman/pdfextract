'''
Utilities to be used through pdftools.
'''


from pathlib import Path


def generate_unique_filename(base_filename="output") -> Path:
    '''
    Generates a unique filename that doesn't conflict with existing files.

    :param base_filename: The name of the file, which this function will add
    numbers to. The output filename will be `base_filename`, an underscore
    (`_`), and the first number that makes the filename unique in the current
    working directory.

    :return: The path of the unique filename.
    '''

    counter = 0
    while True:
        filename = Path(f"{base_filename}_{counter}.pdf")
        if not filename.exists():
            break
        counter += 1
    return filename
