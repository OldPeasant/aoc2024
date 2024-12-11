import sys

sys.setrecursionlimit(10000)

lengths = {}

def transform(n):
    new_stones = []
    if n == 0:
        new_stones.append(1)
    elif len(str(n)) % 2 == 0:
        st = str(n)
        new_stones.append(int(st[:len(st) // 2 ]))
        new_stones.append(int(st[len(st) // 2 :]))
    else:
        new_stones.append(n * 2024)
    return new_stones

def find_len(s, n):
    print("find_len", s, n)
    if s not in lengths:
        lengths[s] = {}
    inner = lengths[s]
    if n in inner:
        return inner[n]
    t = transform(s)
    if n == 1:
        inner[n] = len(t)
        return len(t)
    total = 0
    for i in t:
        l = find_len(i, n - 1)
        total += l
    inner[n] = total
    return total

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()[0]

    stones = [int(s) for s in lines.split(' ')]

    print(stones)
    tot = 0
    for s in stones:
        tot += find_len(s, 75)
    print(tot)

    #for i in range(25):
    #    new_stones = []
    #    for s in stones:
    #        new_stones.extend(transform(s))
    #    stones = new_stones
    #    print(len(stones))
    #print(len(stones))
