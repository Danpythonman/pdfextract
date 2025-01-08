'''
Functionality for initializing and running the pdftools command-line interface.
'''


import argparse

from pdftools.interface.cli.extract_subparser import \
    initialize_extract_subparser, \
    extract_pdf_pages
from pdftools.interface.cli.merge_subparser import \
    initialize_merge_subparser, \
    merge_pdf_files


def initialize_parser() -> argparse.ArgumentParser:
    '''
    Initializes the CLI parser by adding and initializing the extract and merge
    subparsers.

    :return: The pdftools CLI parser.
    '''

    # Top-level CLI argument parser
    parser = argparse.ArgumentParser(
        description='PDF tools.'
    )

    # Subparser for subcommands
    subparsers = parser.add_subparsers(
        title='subcommands',
        dest='command',
        required=True
    )

    # Parser for `extract` subcommand
    parser_extract = subparsers.add_parser(
        'extract',
        help='Extracts pages from a PDF.'
    )

    initialize_extract_subparser(parser_extract)

    # Parser for `merge` subcommand
    parser_merge = subparsers.add_parser(
        'merge',
        help='Merges PDFs into a single PDF.'
    )

    initialize_merge_subparser(parser_merge)

    return parser


def run_pdftools_cli():
    '''
    Runs the pdftools CLI.
    '''

    parser = initialize_parser()

    args = parser.parse_args()

    if args.command == 'extract':
        extract_pdf_pages(parser, args)
    elif args.command == 'merge':
        merge_pdf_files(parser, args)
    else:
        raise argparse.ArgumentError(
            f'Invalid subcommand {args.command}, must be either extract or '
                'merge.'
        )
