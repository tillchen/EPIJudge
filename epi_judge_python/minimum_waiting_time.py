from typing import List

from test_framework import generic_test
from itertools import accumulate


def minimum_total_waiting_time(service_times: List[int]) -> int:
    return sum(list(accumulate(sorted(service_times)))[:-1])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_waiting_time.py',
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
