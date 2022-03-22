from test_framework import generic_test


# Hello_World! (Sinusoidally first, and then left to right, top to bottom)
#   e       _       l
# H   l   o   W   r   d
#       l       o       !
# Result: e_lHloWrdlo!
def snake_string_0(s: str) -> str:
    result = ''
    for i in range(1, len(s), 4):
        result += s[i]
    for i in range(0, len(s), 2):
        result += s[i]
    for i in range(3, len(s), 4):
        result += s[i]
    return result

def snake_string(s: str) -> str:
    return s[1::4] + s[::2] + s[3::4]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',
                                       snake_string))
