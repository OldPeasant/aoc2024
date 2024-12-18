import sys

dirs = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    size = 71

    limit = 1020
    while True:
        field = []
        dist = []
        for row in range(size):
            h = []
            h2 = []
            for col in range(size):
                h.append('.')
                h2.append(None)
            field.append(h)
            dist.append(h2)
        for l in lines[:limit]:
            (x, y) = (int(c) for c in l.split(","))
            field[y][x] = '#'

        #for y in range(size):
        #    print("".join(field[y]))

        l = 0
        points = [ (0, 0) ]
        while dist[size-1][size-1] is None:
            l += 1
            new_points = []
            for p in points:
                for d in dirs:
                    n = (p[0] + d[0], p[1] + d[1])
                    if n[0] >= 0 and n[1] >= 0 and n[0] < size and n[1] < size:
                        c = dist[n[1]][n[0]]
                        if field[n[1]][n[0]] == '.' and (c is None or c > l):
                            dist[n[1]][n[0]] = l
                            new_points.append(n)
            points = new_points
            #print(points)
            if len(points) == 0:
                print("No path")
                print(lines[limit-1])
                exit(0)
        print("best path len", limit, dist[size-1][size-1])
        #for y in range(size):
        #    print("".join( (c if dist[y][ix_c] is None else 'O') for ix_c, c in enumerate(field[y])))
        limit += 1
