'''
The top-level module for the pdftools command-line interface.
'''


from .pdftools_parser import run_pdftools_cli


def main():
    '''
    The main entry point for the pdftools CLI.
    '''

    run_pdftools_cli()
