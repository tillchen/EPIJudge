from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:

    SCALE_FACTOR = 2

    def __init__(self, capacity: int) -> None:
        self.entries = [None] * capacity
        self.num_of_entries = self.head = self.tail = 0
        return

    def enqueue(self, x: int) -> None:
        if self.num_of_entries == len(self.entries):
            # Expand the queue.
            self.entries = self.entries[self.head:] + self.entries[:self.head]
            self.head = 0
            self.tail = self.num_of_entries
            self.entries += [None] * len(self.entries) * (Queue.SCALE_FACTOR - 1)
        self.entries[self.tail] = x
        self.tail = (self.tail + 1) % len(self.entries)
        self.num_of_entries += 1
        return

    def dequeue(self) -> int:
        if self.num_of_entries == 0:
            raise IndexError('Empty queue')
        result = self.entries[self.head]
        self.head = (self.head + 1) % len(self.entries)
        self.num_of_entries -= 1
        return result

    def size(self) -> int:
        return self.num_of_entries


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
