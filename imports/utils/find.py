from .common.file_operation import save_to_file,read_file
class NotFoundError(Exception):
    def __init__(self):
        super().__init__()
def find_in(iterable,finder,expected):
    for i in iterable:
        if finder(i) == expected:
            return i
    raise NotFoundError(f"{expected} not found in {iterable}.")


print(__name__)