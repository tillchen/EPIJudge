from typing import List

from test_framework import generic_test


# 19216811 -> 192.168.1.1, 19.216.81.1, etc.
def get_valid_ip_address(s: str) -> List[str]:
    def is_sub_part_valid(part: str) -> bool:
        return len(part) == 1 or (part[0] != '0' and int(part) < 256)

    result = []
    parts = [None] * 4
    for i in range(1, min(4, len(s))):
        parts[0] = s[:i]
        if is_sub_part_valid(parts[0]):
            for j in range(1, min(4, len(s) - i)):
                parts[1] = s[i:i+j]
                if is_sub_part_valid(parts[1]):
                    for k in range(1, min(4, len(s) - i - j)):
                        parts[2], parts[3] = s[i+j:i+j+k], s[i+j+k:]
                        if is_sub_part_valid(parts[2]) and is_sub_part_valid(parts[3]):
                            result.append('.'.join(parts))
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
