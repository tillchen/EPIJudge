from typing import List

from test_framework import generic_test
import heapq


def merge_sorted_arrays_0(sorted_arrays: List[List[int]]) -> List[int]:
    return list(heapq.merge(*sorted_arrays))

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    sorted_array_iters = [iter(x) for x in sorted_arrays]
    result = []
    min_heap = []
    for i, it in enumerate(sorted_array_iters):
        first = next(it, None)
        if first is not None:
            heapq.heappush(min_heap, (first, i))
    while min_heap:
        smallest_entry, smallest_index = heapq.heappop(min_heap)
        result.append(smallest_entry)
        smallest_iter = sorted_array_iters[smallest_index]
        next_entry = next(smallest_iter, None)
        if next_entry is not None:
            heapq.heappush(min_heap, (next_entry, smallest_index))
    return result



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
