from test_framework import generic_test


def test_collatz_conjecture(n: int) -> bool:
    verified_numbers = set()
    for i in range(3, n + 1):
        sequence = set()
        current = i
        while current >= i:
            if current in sequence:
                # Infinite loop.
                return False
            sequence.add(current)
            if current % 2 == 1:
                if current in verified_numbers:
                    break
                verified_numbers.add(current)
                current = current * 3 + 1
            else:
                current //= 2
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('collatz_checker.py',
                                       'collatz_checker.tsv',
                                       test_collatz_conjecture))
