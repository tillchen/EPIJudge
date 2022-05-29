from test_framework import generic_test

from collections import Counter


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    return Counter(magazine_text) | Counter(letter_text) == Counter(magazine_text)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
