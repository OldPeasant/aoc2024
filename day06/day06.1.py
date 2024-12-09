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
    for l in safe:
        print(l)
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

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
    safe_lines = border(lines)
    (row, col) = find_start(safe_lines)
    print("coords", row, col)
    
    safe_lines[row][col] = '.'
    for l in safe_lines:
        print(l)

    direction = (-1, 0)

    visited = set()
    visited.add( (row, col))
    width = len(safe_lines[0])
    height = len(safe_lines)
    while True: #row > 0 and row < height - 1 and col > 0 and col < width - 1:
        next_row = row + direction[0]
        next_col = col + direction[1]
        if next_row == 0 or next_col == 0 or next_row == height -1 or next_col == width - 1:
            break
        if safe_lines[next_row][next_col] == '#':
            direction = TURN[direction]
        else:
            row = next_row
            col = next_col
            visited.add((row, col))
        print(direction, row, col)
    print(len(visited))



