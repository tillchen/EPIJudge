from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    memo = [[-1] * len(B) for _ in range(len(A))]
    def helper(A_index: int, B_index: int) -> int:
        if A_index < 0:
            return B_index + 1
        if B_index < 0:
            return A_index + 1
        if memo[A_index][B_index] == -1:
            if A[A_index] == B[B_index]:
                memo[A_index][B_index] = helper(A_index - 1, B_index - 1)
            else:
                substitute_last = helper(A_index - 1, B_index - 1)
                add_last = helper(A_index - 1, B_index)
                delete_last = helper(A_index, B_index - 1)
                memo[A_index][B_index] = 1 + min(substitute_last, add_last, delete_last)
        return memo[A_index][B_index]
    return helper(len(A) - 1, len(B) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
