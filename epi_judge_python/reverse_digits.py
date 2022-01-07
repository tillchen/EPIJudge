from test_framework import generic_test

def reverse_0(x: int) -> int:
    # Reverse an integer.
    return int(str(x)[::-1]) if x >= 0 else - int(str(x)[1:][::-1])


def reverse(x: int) -> int:
    # Reverse an integer.
    sign = 1 if x >= 0 else -1
    result = 0
    x = abs(x)
    while x:
        current_digit = x % 10
        x //= 10
        result = result * 10 + current_digit
    return result * sign


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
