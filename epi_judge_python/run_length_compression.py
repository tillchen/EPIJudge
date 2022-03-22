from test_framework import generic_test
from test_framework.test_failure import TestFailure
from itertools import groupby


# 4a1b3c2a -> aaaabcccaa
def decoding(s: str) -> str:
    i, j = 0, 1
    result = ''
    while i < len(s) and j < len(s):
        while j < len(s) and s[j].isdecimal():
            j += 1
        result += ''.join([s[j]] * int(s[i:j]))
        i = j + 1
        j = i + 1
    return result


# aaaabcccaa -> 4a1b3c2a
def encoding_0(s: str) -> str:
    return ''.join([f'{len(list(v))}{k}' for k, v in groupby(s)])

def encoding_1(s: str) -> str:
    result = ''
    i = 0
    while i + 1 < len(s):
        local_count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            local_count += 1
            i += 1
        result += f'{local_count}{s[i]}'
        i += 1
    if len(s) == 1 or s[-2] != s[-1]:
        result += f'1{s[-1]}'
    return result

def encoding(s: str) -> str:
    result = ''
    count = 1
    for i in range(1, len(s) + 1):
        if i == len(s) or s[i - 1] != s[i]:
            result += f'{count}{s[i - 1]}'
            count = 1
        else:
            count += 1
    return result

def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
