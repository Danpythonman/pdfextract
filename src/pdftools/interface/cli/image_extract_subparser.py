'''
Functions for initializing the subparser for the `merge` subcommand and
executing the PDF merge algorithm.
'''


import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

from pdftools.merge import merge_pdfs


@dataclass
class PdfMergeDto:
    '''
    Data transfer object for the arguments of the `merge` subcommand.
    '''

    input_filepaths: List[Path]
    '''
    The list of file paths of the input PDF files.
    '''

    outfile: Optional[Path]
    '''
    The name of the output PDF file.
    '''


def verify_and_parse_merge_args(
    parser: argparse.ArgumentParser,
    args: argparse.Namespace
):
    '''
    Verifies parser arguments for the `merge` subcommand and parses them into a
    DTO.

    :param parser: The command line parser. (Used for outputting error
    messages.)

    :param args: The command line arguments.

    :return: The arguments parsed into a DTO.
    '''

    input_filepaths = []
    for filename in args.file_list:
        filepath = Path(filename)
        if not filepath.is_file():
            parser.error(f'Error: {filename} is not a file')
        input_filepaths.append(filepath)

    outfile: Optional[Path]
    if args.outfile:
        outfile = Path(args.outfile)
    else:
        outfile = None

    return PdfMergeDto(input_filepaths, outfile)


def merge_pdf_files(parser: argparse.ArgumentParser, args: argparse.Namespace):
    '''
    Verifies the command line arguments for the `merge` subcommand and runs
    the PDF merging algorithm.

    :param parser: The command line parser.

    :param args: The command line arguments.
    '''

    pdf_merge_dto = verify_and_parse_merge_args(parser, args)

    print('Merging PDFs:')
    for pdf_file in pdf_merge_dto.input_filepaths:
        print(f'  -{pdf_file.absolute()}')

    output_pdf_path = merge_pdfs(
        pdf_merge_dto.input_filepaths,
        pdf_merge_dto.outfile
    )

    print(f'PDFs merged to {output_pdf_path.absolute()}')


def initialize_merge_subparser(parser_merge: argparse.ArgumentParser):
    '''
    Initializes the subparser for the `merge` subcommand by declaring its
    arguments.

    :param parser_merge: The subparser for the `merge` subcommand.
    '''

    parser_merge.add_argument(
        'file_list',
        nargs='+',
        help='A list of file names.',
    )

    parser_merge.add_argument(
        '-o',
        '--outfile',
        type=str,
        help='The name of the output file.'
    )
