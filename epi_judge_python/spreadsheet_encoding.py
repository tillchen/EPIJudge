from test_framework import generic_test
from functools import reduce

# AA -> 27, AB -> 28
def ss_decode_col_id(col: str) -> int:
    return reduce(lambda a, b: a * 26 + ord(b) - ord('A') + 1, col, 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
