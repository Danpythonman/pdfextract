import argparse
from pathlib import Path
from typing import List

from pdftools.extract import extract_pages


def validate_page_list(page_numbers: str) -> List[int]:
    '''
    Validate a single page number or a list of page numbers.

    :param page_numbers: A string of comma-separated numbers.

    :return: The list of page numbers parsed into a list of integers.

    :raises argparse.ArgumentTypeError: If any of the numbers are negative.
    '''

    pages = [int(x) for x in page_numbers.split(',') if x.strip().isdigit()]
    if any(p <= 0 for p in pages):
        raise argparse.ArgumentTypeError(
            'All page numbers must be positive integers.'
        )
    return pages


def main():
    parser = argparse.ArgumentParser(
        description='PDF tools.'
    )

    subparsers = parser.add_subparsers(
        title='subcommands',
        dest='command',
        required=True
    )

    parser_extract = subparsers.add_parser(
        'extract',
        help='Extracts pages from a PDF.'
    )

    parser_extract.add_argument(
        'filename',
        type=str,
        help='The name of the file to process.'
    )

    parser_extract.add_argument(
        'page_list',
        type=validate_page_list,
        nargs='?',
        help='A list of specific page numbers separated by commas '
            '(e.g., 1,5,8,9).'
    )

    group = parser_extract.add_mutually_exclusive_group()
    group.add_argument(
        '-r',
        '--range',
        nargs=2,
        type=int,
        metavar=('START', 'END'),
        help='A range of page numbers (start and end).'
    )
    group.add_argument(
        '-l',
        '--list',
        type=validate_page_list,
        help='A list of specific page numbers separated by commas '
            '(e.g., 1,5,8,9).'
    )

    parser_extract.add_argument(
        '-o',
        '--outfile',
        type=str,
        help='The name of the output file.'
    )

    args = parser.parse_args()

    input_file_path = Path(args.filename)

    if not input_file_path.exists():
        parser.error(f'Input file {input_file_path} does not exist')

    if not input_file_path.is_file():
        parser.error(f'Input file {input_file_path} is not a file')

    if not args.page_list and not args.range and not args.list:
        parser.error('one of page_files, --list, or --range must be specified')

    if args.page_list and (args.range or args.list):
        parser.error(
            'only one of page_files, --list, or --range can be specified'
        )

    print(f'Processing file {input_file_path.absolute()}...')

    page_list: List[int]

    if args.range:
        start_page, end_page = args.range

        if start_page <= 0 or end_page <= 0:
            parser.error('Page numbers in range must be positive.')

        if end_page < start_page:
            parser.error(
                'End page must be greater than or equal to start page.'
            )

        print(
            f'Processing range from page {start_page} to {end_page} '
                '(inclusive)...'
        )
        page_list = list(range(start_page, end_page + 1))
    elif args.page_list:
        page_list = args.page_list
    elif args.list:
        page_list = args.list
    else:
        parser.error('no pages were specified to be extracted')

    print(f'Extracting pages {page_list}...')

    if args.outfile:
        output_pdf_path = extract_pages(
            input_file_path,
            page_list,
            Path(args.outfile)
        )
    else:
        output_pdf_path = extract_pages(input_file_path, page_list)

    print(f'Pages extracted to {output_pdf_path.absolute()}')


if __name__ == '__main__':
    main()
