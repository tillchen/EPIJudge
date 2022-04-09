from typing import Iterator, List

from test_framework import generic_test


# sequence is east to west. Any building shorter than or equal to the building on the west can't see the sunset.
# Building on the east side of a taller/equal building can't see.
# e.g 5,4,3,2,1 all fine. 5,6,2,7,1 -> 7, 1
# We return the indices.
def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    if not sequence:
        return []
    result = [len(sequence) - 1]
    for i in reversed(range(len(sequence) - 1)):
        if sequence[i] > sequence[result[-1]]:
            result.append(i)
    return result


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
