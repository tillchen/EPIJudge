import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from collections import defaultdict

Point = collections.namedtuple('Point', ('x', 'y'))


def find_line_with_most_points(points: List[Point]) -> int:
    result = 0
    for i, point in enumerate(points):
        slopes = defaultdict(int)
        duplicate_points = 1
        for j in range(i + 1, len(points)):
            if point == points[j]:
                duplicate_points += 1
            elif point.x == points[j].x:
                slopes[float('inf')] += 1
            else:
                x_diff = point.x - points[j].x
                y_diff = point.y - points[j].y
                slopes[y_diff / x_diff] += 1
        result = max(result, max(slopes.values(), default=0) + duplicate_points)
    return result


@enable_executor_hook
def find_line_with_most_points_wrapper(executor, points):
    points = [Point(*x) for x in points]
    return executor.run(functools.partial(find_line_with_most_points, points))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('line_through_most_points.py',
                                       'line_through_most_points.tsv',
                                       find_line_with_most_points_wrapper))
