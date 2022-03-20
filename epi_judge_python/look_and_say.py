from test_framework import generic_test
from itertools import groupby

# 1, 11, 21, 1211, 111221, 312211
def look_and_say_0(n: int) -> str:
    s = '1'
    def next_number(s: str) -> str:
        i = 0
        result = ''
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
                i += 1
            result += f'{count}{s[i]}'
            i += 1
        return result

    for _ in range(n - 1):
        s = next_number(s)
    return s


def look_and_say(n: int) -> str:
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(list(value))) + key for key, value in groupby(s))
    return s


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
