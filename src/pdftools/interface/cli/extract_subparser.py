'''
Functions for initializing the subparser for the `extract` subcommand and
executing the PDF page extraction algorithm.
'''


import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

from pdftools.extract import extract_pages


@dataclass
class PdfExtractDto:
    '''
    Data transfer object for the arguments of the `extract` subcommand.
    '''

    input_file_path: Path
    '''
    The file path of the input PDF file.
    '''

    page_list: List[int]
    '''
    The list of page numbers to extract from the input PDF file.
    '''

    outfile: Optional[Path]
    '''
    The name of the output PDF file.
    '''


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


def verify_and_parse_extract_args(
    parser: argparse.ArgumentParser,
    args: argparse.Namespace
) -> PdfExtractDto:
    '''
    Verifies parser arguments for the `extract` subcommand and parses them into
    a DTO.

    :param parser: The command line parser. (Used for outputting error
    messages.)

    :param args: The command line arguments.

    :return: The arguments parsed into a DTO.
    '''

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

    outfile: Optional[Path]
    if args.outfile:
        outfile = Path(args.outfile)
    else:
        outfile = None

    return PdfExtractDto(input_file_path, page_list, outfile)


def extract_pdf_pages(parser: argparse.ArgumentParser, args: argparse.Namespace):
    '''
    Verifies the command line arguments for the `extract` subcommand and runs
    the PDF page extraction algorithm.

    :param parser: The command line parser.

    :param args: The command line arguments.
    '''

    pdf_extract_dto = verify_and_parse_extract_args(parser, args)

    print(
        f'Extracting pages {pdf_extract_dto.page_list} from '
            f'{pdf_extract_dto.input_file_path.absolute()}...'
    )

    output_pdf_path = extract_pages(
        pdf_extract_dto.input_file_path,
        pdf_extract_dto.page_list,
        pdf_extract_dto.outfile
    )

    print(f'Pages extracted to {output_pdf_path.absolute()}')


def initialize_extract_subparser(parser_extract: argparse.ArgumentParser):
    '''
    Initializes the subparser for the `extract` subcommand by declaring its
    arguments.

    :param parser_extract: The subparser for the `extract` subcommand.
    '''

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
