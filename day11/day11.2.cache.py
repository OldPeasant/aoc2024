from sys import argv
from functools import cache

@cache
def find_len(s, n):
    ss = str(s)
    if n == 1:
        return 2 if len(ss) % 2 == 0 else 1
    if s == 0:
        return find_len(1, n-1)
    elif len(ss) % 2 == 0:
        t = [int(ss[:len(ss) // 2 ]), int(ss[len(ss) // 2 :])]
        return sum(find_len(i, n - 1) for i in t)
    else:
        return find_len(s * 2024, n-1)

with open(argv[1]) as f:
    lines = f.read().splitlines()[0]
    stones = [int(s) for s in lines.split(' ')]
    print(sum(find_len(s, 75) for s in stones))
