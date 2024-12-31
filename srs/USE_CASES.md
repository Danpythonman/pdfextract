# Use Case Document

This document is used to describe the use cases of `pdfextract` to streamline the development of functional and nonfunctional requirements.

## Use Case 1: Extracting a single page from a PDF

- **Primary Actor:** A user with a multi-page PDF file who needs only a single page from the file.

- **Preconditions:** The user must have a PDF file with more than one page.

- **Postconditions:** The user will have a new PDF file generated consisting of the single page they specified.

- **Exceptions:**

    - **If** the PDF file has only 1 page,

      **Then** the system should function normally as long as the user specified page 1 to be extracted. Otherwise, an error message will be shown to the user, no output file will be generated.

    - **If** the user specifies a page number not in the PDF,

      **Then** an error message will be shown to the user, no output file will be generated.

## Use Case 2: Extracting a list of pages from a PDF

- **Primary Actor:** A user with a multi-page PDF file who needs multiple, potentially non-consecutive pages from the file.

- **Preconditions:** The user must have a PDF file with more than one page.

- **Postconditions:** The user will have a new PDF file generated consisting of the pages they specified from the original PDF.

- **Exceptions:**

    - **If** The user specifies one or more page numbers that are not in the file,

      **Then** an error message will be shown to the user informing the user of all the page numbers that are out of bounds, no output file generated.

## Use Case 3: Extracting a range of pages from a PDF

- **Primary Actor:** A user with a multi-page PDF file who needs multiple consecutive pages from the file.

- **Preconditions:** The user must have a PDF file with more than one page.

- **Postconditions:** The user will have a new PDF file generated consisting of the range of pages they specified from the original PDF.

- **Exceptions:**

    - **If** The page number of the start of range is not in the file,

      **Then** an error message will be shown to the user informing the user that the start of the range is out of bounds, no output file generated.

    - **If** The page number of the end of range is not in the file,

      **Then** an error message will be shown to the user informing the user that the end of the range is out of bounds, no output file generated.

    - **If** The page numbers of the start and end of range are not in the file,

      **Then** an error message will be shown to the user informing the user that the start and end of the range are out of bounds, no output file generated.

## Use Case 4: User naming the output file

- **Primary Actor:** A user with a PDF file who needs pages from the file as a new PDF file with a specific filename.

- **Preconditions:** The user must have a PDF file and a name for the output file.

- **Postconditions:** The user will have a new PDF file with the name they specified, generated consisting of the pages they specified from the original PDF.

- **Exceptions:**

    - **If** The user specifies a path for the output file, but one or more of the directories in the path do not exist,

      **Then** an error message will be shown to the user informing the user that the path they specified does not exist, no output file generated.

## Use Case 5: Automatic naming the output file

- **Primary Actor:** A user with a PDF file who needs pages from the file as a new PDF file without a specific filename.

- **Preconditions:** The user must have a PDF file.

- **Postconditions:** The user will have a new PDF file in their working directory with a name that does not conflict with any of the files in the directory, generated consisting of the pages they specified from the original PDF.
