from test_framework import generic_test
from test_framework.test_failure import TestFailure

import bintrees


class ClientsCreditsInfo:

    def __init__(self) -> None:
        self.offset = 0
        self.client_id_to_credit = {}
        self.credit_to_client_ids = bintrees.RBTree()

    def insert(self, client_id: str, c: int) -> None:
        self.remove(client_id)
        self.client_id_to_credit[client_id] = c - self.offset
        self.credit_to_client_ids.setdefault(c - self.offset, set()).add(client_id)
        return

    def remove(self, client_id: str) -> bool:
        credit = self.client_id_to_credit.get(client_id)
        if credit is not None:
            self.credit_to_client_ids[credit].remove(client_id)
            if not self.credit_to_client_ids[credit]:
                del self.credit_to_client_ids[credit]
            del self.client_id_to_credit[client_id]
            return True
        return False

    def lookup(self, client_id: str) -> int:
        if client_id not in self.client_id_to_credit:
            return -1
        return self.client_id_to_credit[client_id] + self.offset

    def add_all(self, C: int) -> None:
        self.offset += C

    def max(self) -> str:
        if not self.credit_to_client_ids:
            return ''
        client_ids = self.credit_to_client_ids
        return '' if not client_ids else next(iter(client_ids))


def client_credits_info_tester(ops):
    cr = ClientsCreditsInfo()

    for x in ops:
        op = x[0]
        s_arg = x[1]
        i_arg = x[2]
        if op == 'ClientsCreditsInfo':
            pass
        if op == 'max':
            result = cr.max()
            if result != s_arg:
                raise TestFailure('Max: return value mismatch')
        elif op == 'remove':
            result = cr.remove(s_arg)
            if result != i_arg:
                raise TestFailure('Remove: return value mismatch')
        elif op == 'insert':
            cr.insert(s_arg, i_arg)
        elif op == 'add_all':
            cr.add_all(i_arg)
        elif op == 'lookup':
            result = cr.lookup(s_arg)
            if result != i_arg:
                raise TestFailure('Lookup: return value mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('adding_credits.py',
                                       'adding_credits.tsv',
                                       client_credits_info_tester))
