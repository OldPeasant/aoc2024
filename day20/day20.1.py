import sys

dirs = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]

def find_best(field, start):

    visited = { start: 0}
    next_pos = [start]
    dist = 0
    while True:
        dist += 1
        new_next = []
        for n in next_pos:
            for d in dirs:
                p = ( n[0] + d[0], n[1] + d[1] )
                c = field[p[0]][p[1]]
                if c == 'E':
                    return dist
                if c == '.':
                    if p not in visited:
                        visited[p] = dist
                        new_next.append(p)
        next_pos = new_next

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    field = []
    for r_ix, l in enumerate(lines):
        row = []
        for c_ix, c in enumerate(l):
            if c == 'S':
                s = (r_ix, c_ix)
            row.append(c)
        field.append(row)

    orig = find_best(field, s)
    cheats = {}
    print("Original", orig)
    for r_ix in range(1, len(lines) - 1):
        print(r_ix)
        for c_ix in range(1, len(lines[0]) - 1):
            if field[r_ix][c_ix] == '#':
                field[r_ix][c_ix] = '.'
                cheat_dist = find_best(field, s)
                delta = orig - cheat_dist
                if delta in cheats:
                    cheats[delta] += 1
                else:
                    cheats[delta] = 1
                field[r_ix][c_ix] = '#'
    solution = 0
    for k in sorted(cheats.keys()):
        print(cheats[k], "cheats save", k)
        if k >= 100:
            solution += cheats[k]
    print(solution)
