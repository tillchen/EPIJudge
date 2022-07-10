import collections
from typing import List

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(task_durations: List[int]) -> List[PairedTasks]:
    task_durations.sort()
    result = []
    i, j = 0, len(task_durations) - 1
    while i < j:
        result.append(PairedTasks(task_durations[i], task_durations[j]))
        i += 1
        j -= 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('task_pairing.py', 'task_pairing.tsv',
                                       optimum_task_assignment))
