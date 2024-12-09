import sys
from itertools import combinations

with open(sys.argv[1]) as f:
    frequencies = {}
    rows = f.read().splitlines()
    for row_ix, row in enumerate(rows):
        for col_ix, col in enumerate(row):
            if col != '.':
                if col not in frequencies:
                    s = set()
                    frequencies[col] = s
                else:
                    s = frequencies[col]
                s.add( (row_ix, col_ix) )
    print(frequencies)
    antinodes = set()
    height = len(rows)
    width = len(rows[0])
    print("height", height, "width", width)
    for f, signals in frequencies.items():
        for s1, s2 in combinations(signals, 2):
            antinodes.add(s1)
            antinodes.add(s2)
            print(f, s1, s2)
            delta1 = (s1[0] - s2[0], s1[1] - s2[1])
            print("delta1", delta1)
            a1 = (s1[0] + delta1[0], s1[1] + delta1[1])
            while a1[0] >= 0 and a1[0] < height and a1[1] >= 0 and a1[1] < width:
                print("a1", a1)
                antinodes.add(a1)
                a1 = (a1[0] + delta1[0], a1[1] + delta1[1])

            delta2 = (s2[0] - s1[0], s2[1] - s1[1])
            print("delta2", delta2)
            a2 = (s2[0] + delta2[0], s2[1] + delta2[1])
            while a2[0] >= 0 and a2[0] < height and a2[1] >= 0 and a2[1] < width:
                print("a2", a2)
                antinodes.add(a2)
                a2 = (a2[0] + delta2[0], a2[1] + delta2[1])
    print(antinodes)
    print(len(antinodes))
