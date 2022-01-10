from test_framework import generic_test
import math

def is_palindrome_number_0(x: int) -> bool:
    return str(x) == str(x)[::-1]

def is_palindrome_number(x: int) -> bool:
    # Check if x is a palindrom.
    if x <= 0:
        return x == 0
    number_of_digits = math.floor(math.log10(x)) + 1
    msn_mask = 10 ** (number_of_digits - 1)
    for i in range(number_of_digits // 2):
        lsn = x % 10
        msn = x // msn_mask
        if lsn != msn:
            return False
        x %= msn_mask
        x //= 10
        msn_mask //= 100
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
