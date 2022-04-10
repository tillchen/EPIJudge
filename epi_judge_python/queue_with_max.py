from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import deque

class QueueWithMax_0:

    def __init__(self) -> None:
        self.queue = deque()

    def enqueue(self, x: int) -> None:
        self.queue.append(x)

    def dequeue(self) -> int:
        return self.queue.popleft()

    def max(self) -> int:
        return max(self.queue)

class QueueWithMax:

    def __init__(self) -> None:
        self.queue = deque()
        self.max_queue = deque()

    def enqueue(self, x: int) -> None:
        self.queue.append(x)
        while self.max_queue and self.max_queue[-1] < x:
            self.max_queue.pop()
        self.max_queue.append(x)

    def dequeue(self) -> int:
        if not self.queue:
            raise IndexError('Empty queue')
        result = self.queue.popleft()
        if result == self.max_queue[0]:
            self.max_queue.popleft()
        return result

    def max(self) -> int:
        if not self.max_queue:
            raise IndexError('Empty queue')
        return self.max_queue[0]

def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_with_max.py',
                                       'queue_with_max.tsv', queue_tester))
