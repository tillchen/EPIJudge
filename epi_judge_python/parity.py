from test_framework import generic_test


def parity(x: int) -> int:
    # 1 if the number of 1 bits is odd. Else 0.
    result = 0
    while x:
        result ^= 1
        x &=  (x - 1) # Remove the lowest set bit.
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
