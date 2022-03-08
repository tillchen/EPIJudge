from typing import List

from test_framework import generic_test

# [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
def generate_pascal_triangle(n: int) -> List[List[int]]:
    result = [[1] * (x + 1) for x in range(n)]
    for i in range(n):
        for j in range(1, i):
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
