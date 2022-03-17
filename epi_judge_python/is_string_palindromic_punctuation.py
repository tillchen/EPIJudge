from test_framework import generic_test
from string import punctuation


def is_palindrome(s: str) -> bool:
    s = s.translate(str.maketrans('', '', punctuation)).replace(' ', '')
    return s == s[::-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
