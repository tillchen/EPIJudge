from test_framework import generic_test
from test_framework.test_failure import TestFailure

from collections import OrderedDict

class LruCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.isbns_to_prices = OrderedDict()
        return

    def lookup(self, isbn: int) -> int:
        if isbn not in self.isbns_to_prices:
            return -1
        self.isbns_to_prices.move_to_end(isbn)
        return self.isbns_to_prices[isbn]

    def insert(self, isbn: int, price: int) -> None:
        if isbn in self.isbns_to_prices:
            self.isbns_to_prices.move_to_end(isbn)
        else:
            if len(self.isbns_to_prices) == self.capacity:
                self.isbns_to_prices.popitem(last=False)
            self.isbns_to_prices[isbn] = price

    def erase(self, isbn: int) -> bool:
        return self.isbns_to_prices.pop(isbn, None) is not None


def lru_cache_tester(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure('Lookup: expected ' + str(cmd[2]) +
                                  ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure('Erase: expected ' + str(cmd[2]) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lru_cache.py', 'lru_cache.tsv',
                                       lru_cache_tester))
