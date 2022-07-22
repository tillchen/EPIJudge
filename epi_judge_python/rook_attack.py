import copy
from typing import List

from test_framework import generic_test

def rook_attack_0(A: List[List[int]]) -> None:
    rows, columns = set(), set()
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 0:
                rows.add(i)
                columns.add(j)
    for i in range(len(A)):
        for j in range(len(A[0])):
            if i in rows or j in columns:
                A[i][j] = 0


def rook_attack(A: List[List[int]]) -> None:
    is_first_row = is_first_column = False
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 0:
                if i == 0:
                    is_first_row = True
                if j == 0:
                    is_first_column = True
                if i != 0 and j != 0:
                    A[0][j] = A[i][0] = 0
    for i in range(1, len(A)):
        if A[i][0] == 0:
            for j in range(1, len(A[0])):
                A[i][j] = 0
    for j in range(1, len(A[0])):
        if A[0][j] == 0:
            for i in range(1, len(A)):
                A[i][j] = 0
    if is_first_row:
        for j in range(len(A[0])):
            A[0][j] = 0
    if is_first_column:
        for i in range(len(A)):
            A[i][0] = 0


def rook_attack_wrapper(A):
    a_copy = copy.deepcopy(A)
    rook_attack(a_copy)
    return a_copy


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rook_attack.py', 'rook_attack.tsv',
                                       rook_attack_wrapper))
