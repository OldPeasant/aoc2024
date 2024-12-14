import sys

mode = {
        '00': ('input-dummy0.txt', 11, 7),
        '0': ('input-dummy.txt', 11, 7),
        '1': ('input.txt', 101, 103)
}

(filename, width, height) = mode[sys.argv[1]]

print("file", filename)
print("width", width)
print("height", height)

def print_robots(robots):
    fld = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(0)
        fld.append(row)
    #print("fld", len(fld), len(fld[0]))
    #print("full fld")
    #print(fld)
    for r in robots:
        col = r[0][0]
        row = r[0][1]
        #print("coord", r, row, col)
        #print("FLD", fld)
        #print("row*", fld[row])
        fld[row][col] += 1
    print("-------")
    for r in fld:
        print("".join((str(p) if p > 0 else '.') for p in r))

with open(filename) as f:

    lines = f.read().splitlines()
    robots = []
    for l in lines:
        pos, velo = l.split(' ')
        p = [int(n) for n in pos.split('=')[1].split(',')]
        v = [int(n) for n in velo.split('=')[1].split(',')]
        #print(p, v)
        robots.append( [p, v] )
    print_robots(robots)
    for i in range(1000000000):
        for ri, r in enumerate(robots):
            nx = r[0][0] + r[1][0]
            ny = r[0][1] + r[1][1]
            while nx < 0:
                nx += width
            while nx >= width:
                nx -= width
            while ny < 0:
                ny += height
            while ny >= height:
                ny -= height
            r[0] = (nx, ny)
        #print(robots)
        print(i)
        print_robots(robots)
        input()
    print_robots(robots)
    mid_x = width // 2
    mid_y = height // 2
    q = {0:0, 1:0, 2:0, 3:0}
    for r in robots:
        (x, y) = r[0]
        if x < mid_x:
            if y < mid_y:
                q[0] += 1
            elif y > mid_y:
                q[1] += 1
        elif x > mid_x:
            if y < mid_y:
                q[2] += 1
            elif y > mid_y:
                q[3] += 1
    print(q)
    result = q[0] * q[1] * q[2] * q[3]
    print(result)
