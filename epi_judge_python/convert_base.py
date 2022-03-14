from test_framework import generic_test
from collections import deque

# Convert num_as_string in b1 base to base b2.
def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    if num_as_string == '0':
        return '0'
    is_negative = False
    if num_as_string[0] == '-':
        is_negative = True
        num_as_string = num_as_string[1:]
    letters_to_nums = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    nums_to_letters = {value: key for key, value in letters_to_nums.items()}
    # Convert to base 10 first.
    num_in_base_10 = 0
    for i, c in enumerate(reversed(num_as_string)):
        if c in letters_to_nums:
            num_to_add = letters_to_nums[c]
        else:
            num_to_add = int(c)
        num_in_base_10 += num_to_add * b1 ** i
    # Convert to base b2.
    num_stack = deque()
    while num_in_base_10:
        num_to_add = num_in_base_10 % b2
        if num_to_add in nums_to_letters:
            char_to_add = nums_to_letters[num_to_add]
        else:
            char_to_add = str(num_to_add)
        num_stack.appendleft(char_to_add)
        num_in_base_10 //= b2
    if is_negative:
        num_stack.appendleft('-')
    return ''.join(num_stack)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
