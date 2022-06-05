import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))
EndPoint = collections.namedtuple('EndPoint', ('time', 'is_start'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    endpoints = [EndPoint(x.start, True) for x in A] + [EndPoint(x.finish, False) for x in A]
    endpoints.sort(key=lambda x: (x.time, not x.is_start))
    result, current_max = 0, 0
    for endpoint in endpoints:
        if endpoint.is_start:
            current_max += 1
            result = max(result, current_max)
        else:
            current_max -= 1
    return result


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
