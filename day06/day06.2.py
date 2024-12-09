import sys

def border(lines):
    width = len(lines[0])
    safe = []
    r = []
    for i in range(width + 2):
        r.append("#")
    safe.append(r)
    for l in lines:
        new_row = []
        new_row.append("#")
        for c in l:
            new_row.append(c)
        new_row.append("#")
        safe.append(new_row)
    r = []
    for i in range(width + 2):
        r.append("#")
    safe.append(r)
    #for l in safe:
    #    print(l)
    return safe

def find_start(lines):
    for row_ix, row in enumerate(lines):
        if "^" in row:
            col_ix = row.index('^')
            return (row_ix, col_ix)

    raise Exception("Start now found")

TURN = {
    (-1, 0) : (0, 1),
    (0, 1) : (1, 0),
    (1, 0) : (0, -1),
    (0, -1) : (-1, 0)
}
def has_loop(safe_lines, start_row, start_col):
    past = set()
    row = start_row
    col = start_col
    direction = (-1, 0)
    past.add( (row, col, direction[0], direction[1]) )
    width = len(safe_lines[0])
    height = len(safe_lines)
    while True:
        next_row = row + direction[0]
        next_col = col + direction[1]
        if next_row == 0 or next_col == 0 or next_row == height -1 or next_col == width - 1:
            #print("This went outside")
            break
        if safe_lines[next_row][next_col] == '#' or safe_lines[next_row][next_col] == 'O':
            direction = TURN[direction]
        else:
            row = next_row
            col = next_col
            #print(direction, row, col)
        st = (row, col, direction[0], direction[1])
        if st in past:
            #print("Loop:", st)
            for p in past:
                if p[0] != start_row or p[1] != start_col:
                    if safe_lines[p[0]][p[1]] == 'O':
                        raise Exception()
                    safe_lines[p[0]][p[1]] = "+"
            
            #for l in safe_lines:
            #    print("".join(l))
            return True
        past.add(st)
    #print("no loop")
    for p in past:
        if p[0] != start_row or p[1] != start_col:
            safe_lines[p[0]][p[1]] = "+"
    #for l in safe_lines:
    #    print("".join(l))
    return False

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
    safe_lines = border(lines)
    (row, col) = find_start(safe_lines)
    
#    safe_lines[row][col] = '.'

    count_loops = 0
    for obst_row in range(1, len(safe_lines) - 1):
        for obst_col in range(1, len(safe_lines[0]) - 1):
            safe_lines = border(lines)
            if obst_row != row or obst_col != col:
                safe_lines[obst_row][obst_col] = "O"
                if has_loop(safe_lines, row, col):
                    count_loops += 1
            #print(obst_row, obst_col, count_loops)
    print(count_loops)

