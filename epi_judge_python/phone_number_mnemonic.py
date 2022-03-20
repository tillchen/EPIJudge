from typing import List

from test_framework import generic_test, test_utils

from itertools import permutations


def phone_mnemonic(phone_number: str) -> List[str]:
    mapping = {
        '0': '0',
        '1': '1',
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PQRS',
        '8': 'TUV',
        '9': 'WXYZ'
    }
    result = ['']
    def helper(phone_number: str):
        if not phone_number:
            return
        nonlocal result
        result = [x + y for x in result for y in mapping[phone_number[0]]]
        helper(phone_number[1:])
    helper(phone_number)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
