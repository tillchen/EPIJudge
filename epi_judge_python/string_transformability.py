from typing import Set

from test_framework import generic_test

from collections import namedtuple
from collections import deque
from string import ascii_lowercase

def transform_string(D: Set[str], s: str, t: str) -> int:
    StringWithDistance = namedtuple('StringWithDistance', ('candidate', 'distance'))
    queue = deque([StringWithDistance(s, 0)])
    D.remove(s)
    while queue:
        current = queue.popleft()
        if current.candidate == t:
            return current.distance
        for i in range(len(s)):
            for c in ascii_lowercase:
                candidate = current.candidate[:i] + c + current.candidate[i+1:]
                if candidate in D:
                    queue.append(StringWithDistance(candidate, current.distance + 1))
                    D.remove(candidate)
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
