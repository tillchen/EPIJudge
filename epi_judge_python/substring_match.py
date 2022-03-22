from test_framework import generic_test

from functools import reduce

def rabin_karp_0(t: str, s: str) -> int:
    return t.index(s) if s in t else -1

def rabin_karp(t: str, s: str) -> int:
    if not t and not s:
        return 0
    if not s:
        return 0
    if not t:
        return -1
    if len(s) > len(t):
        return -1
    BASE = 26
    t_hash = reduce(lambda x, y: x * BASE + ord(y), t[:len(s)], 0)
    s_hash = reduce(lambda x, y: x * BASE + ord(y), s, 0)
    power_s = BASE ** (len(s) - 1)
    for i in range(len(s), len(t)):
        if t_hash == s_hash and t[i-len(s):i] == s:
            return i - len(s)
        # Rolling hash
        t_hash -= ord(t[i-len(s)]) * power_s
        t_hash = t_hash * BASE + ord(t[i])
    if t_hash == s_hash and t[-len(s):] == s:
        return len(t) - len(s)
    return -1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
