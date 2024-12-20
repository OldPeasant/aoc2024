import sys

dirs = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]

def find_distances(field, start):

    visited = { start: 0}
    next_pos = [start]
    dist = 0
    while len(next_pos) > 0:
        #print(next_pos)
        dist += 1
        new_next = []
        for n in next_pos:
            for d in dirs:
                p = ( n[0] + d[0], n[1] + d[1] )
                c = field[p[0]][p[1]]
                if c in ['.', 'E'] and p not in visited:
                    visited[p] = dist
                    new_next.append(p)
        next_pos = new_next
    return visited

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    field = []
    for r_ix, l in enumerate(lines):
        row = []
        for c_ix, c in enumerate(l):
            if c == 'S':
                s = (r_ix, c_ix)
            if c == 'E':
                e = (r_ix, c_ix)
            row.append(c)
        field.append(row)

    distances = find_distances(field, s)
    #print(e)
    #for k, v in distances.items():
    #    print("Dist", k, v)
    #print(distances[e])
    cheats = {}
    for start_row_ix in range(len(field)):
        print(start_row_ix)
        for start_col_ix in range(len(field[0])):
            if field[start_row_ix][start_col_ix] in ['S', '.']:
                #print("Check cheats starting at", start_row_ix, start_col_ix)
                deltas = set()
                for cl in range(2, 21):
                    #print("  Cheat length", cl)
                    for x in range(-cl, cl + 1):
                        for y in [cl - abs(x), -cl + abs(x)]:
                            deltas.add( (x, y) )
                for d in deltas:
                    end_row_ix = start_row_ix + d[0]
                    end_col_ix = start_col_ix + d[1]
                    if  end_row_ix > 0 and end_row_ix < len(field)-1 and end_col_ix > 0 and end_col_ix < len(field[0]) - 1 and field[end_row_ix][end_col_ix] in ['.', 'E']:
                        #print("Should check cheat from", start_row_ix, start_col_ix, "to", end_row_ix, end_col_ix)
                        nl = abs(d[0]) + abs(d[1])
                        #print("Normal length would be", nl)
                        #print("End pos", distances[(end_row_ix, end_col_ix)], "start", distances[(start_row_ix, start_col_ix)])
                        #print("Cheat dist", distances[(end_row_ix, end_col_ix)] - distances[(start_row_ix, start_col_ix)])
                        saved = distances[(end_row_ix, end_col_ix)] - distances[(start_row_ix, start_col_ix)] - nl
                        #print("Saved", saved)
                        if saved > 0:
                            #print("SOL cheat length", cl, "saves", saved)
                            if saved in cheats:
                                cheats[saved] += 1
                            else:
                                cheats[saved] = 1
                    #    print("    x", x, "y", y)
                    #for d in [ (1, 1), (1, -1), (-1,1), (-1, -1) ]:
                    #    print("      d", d)
                    #    print("      cl-x", cl-x)
                    #    end_row_ix = start_row_ix + x * d[0]
                    #    end_col_ix = start_col_ix + (cl - x) * d[1]
                    #    print("      Would check cheating from", start_row_ix, start_col_ix, "to", end_row_ix, end_col_ix)
    #print("Original", orig)
    solution = 0
    for k in sorted(cheats.keys()):
        print(cheats[k], "cheats save", k)
        if k >= 100:
            solution += cheats[k]
    print(solution)
