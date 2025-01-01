from pathlib import Path


class PyPDFNotFoundException(Exception):
    '''
    Exception representing the scenario where a user's system does not have the
    `pypdf` Python library installed.
    '''

    def __init__(self):
        super().__init__(
            'pypdf is not installed\n\nuse pip install pypdf to '
                'install it'
        )


class ParentDirectoryDoesNotExistException(Exception):
    '''
    Exception representing the scenario where a user specified an output file
    path whose directory structure does not exist.
    '''

    def __init__(self, path: Path):
        super().__init__(
            f'The path {path.absolute()} has directories that do not '
                'exist. Please make the directories with\n\n'
                f'mkdir -p {path.parent.absolute()}'
        )
