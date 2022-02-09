from typing import List

from test_framework import generic_test

# e.g. perm = [2, 1, 0, 3] A = [a, b, c, d] -> [c, b, a, d]
def apply_permutation_brute_force(perm: List[int], A: List[int]) -> None:
    result = [0] * len(A)
    for i in range(len(A)):
        result[perm[i]] = A[i]
    A[:] = result

def apply_permutation(perm: List[int], A: List[int]) -> None:
    for i in range(len(A)):
        next_ = i
        while perm[next_] >= 0:
            A[i], A[perm[next_]] = A[perm[next_]], A[i]
            temp = perm[next_]
            # Subtract len(A) to make the element negative, indicating it's visited.
            perm[next_] -= len(A)
            next_ = temp
    # Restore perm
    perm = [x + len(A) for x in perm]

def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
