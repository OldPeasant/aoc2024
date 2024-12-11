import sys

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()[0]

    stones = [int(s) for s in lines.split(' ')]

    print(stones)
    for i in range(25):
        new_stones = []
        for s in stones:
            if s == 0:
                new_stones.append(1)
            elif len(str(s)) % 2 == 0:
                st = str(s)
                new_stones.append(int(st[:len(st) // 2 ]))
                new_stones.append(int(st[len(st) // 2 :]))
            else:
                new_stones.append(s * 2024)
        stones = new_stones
        print(len(stones))
    print(len(stones))
