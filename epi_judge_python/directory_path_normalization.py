from test_framework import generic_test
from collections import deque


def shortest_equivalent_path(path: str) -> str:
    if not path:
        return path
    stack = deque()
    for x in path.split('/'):
        if x == '..':
            if stack and stack[-1] != '..':
                stack.pop()
            else:
                stack.append('..')
        elif x and x != '.':
            stack.append(x)
    result = '/'.join(stack)
    return '/' + result if path[0] == '/' else result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
