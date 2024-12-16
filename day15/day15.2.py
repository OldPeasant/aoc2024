import sys

dirs = {
        '^' : (-1, 0),
        'v' : (1, 0),
        '>' : (0, 1),
        '<' : (0, -1)
}

opposite_dirs = { '^' : 'v', 'v' : '^', '<' : '>', '>' : '<' }

def find_at(field):
    for row_ix, row in enumerate(field):
        for col_ix, c in enumerate(row):
            if c == '@':
                return (row_ix, col_ix)
    raise Exception("@ not found")

def do_move_horizontal(field, row, col, d):
    print("do_move_horizontal", row, col, d)
    nx_row = row
    nx_col = col + d
    if field[nx_row][nx_col] == '.':
        print("next is empty, so move")
        # simple move
        field[nx_row][nx_col] = '@'
        field[row][col] = '.'
        return (nx_row, nx_col)
    print("next is not empty")
    if field[nx_row][nx_col] == '#':
        print("it's a # so abort mission")
        return (row, col)
    print("next is actually a ", field[nx_row][nx_col])
    while field[nx_row][nx_col] in ['[', ']']:
        print("next is O")
        nx_col += d
    if field[nx_row][nx_col] == '#':
        print("bumped into #")
        return (row, col)
    print("This should be a dot", field[nx_row][nx_col])
    print("nx_col", nx_col, "col", col)
    while nx_col != col:
        print("Moving ", nx_col - d, "to", nx_col)
        field[nx_row][nx_col] = field[nx_row][nx_col - d]
        nx_col = nx_col - d
    print("finally", row, col, "to . and ", row, col + d, " to @")
    field[row][col] = '.'
    field[row][col + d] = '@'
    return ( row, col + d)

class Box:
    def __init__(self, row, c1, c2):
        self.row = row
        self.c1 = c1
        self.c2 = c2

def find_next_box(field, nx_row, nx_col, d):
    c = field[nx_row][nx_col]
    if c == '[':
        assert field[nx_row][nx_col + 1] == ']'
        return Box(nx_row, nx_col, nx_col + 1)
    elif c == ']':
        assert field[nx_row][nx_col - 1] == '['
        return Box(nx_row, nx_col - 1, nx_col)
    raise Exception(f"expected [ or ], found {c}")

def find_boxes(field, boxes, d):
    ix = 0
    while ix < len(boxes):
        box = boxes[ix]
        above_left = field[box.row + d][box.c1]
        above_right = field[box.row + d][box.c2]
        if above_left == '#' or above_right == '#':
            return False
        if above_left == ']':
            assert field[box.row + d][box.c1 - 1] == '['
            boxes.append(Box(box.row + d, box.c1 - 1, box.c1))
        if above_right == '[':
            assert field[box.row + d][box.c2 + 1] == ']'
            boxes.append(Box(box.row + d, box.c2, box.c2 + 1))
        if above_left == '[' and above_right == ']':
            boxes.append(Box(box.row + d, box.c1, box.c2))
        ix += 1
    return True

def move_box_vertical(field, d, b):
    field[b.row + d][b.c1] = field[b.row][b.c1]
    field[b.row][b.c1] = '.'
    field[b.row + d][b.c2] = field[b.row][b.c2]
    field[b.row][b.c2] = '.'

def do_move_vertical(field, row, col, d):
    nx_row = row + d
    nx_col = col
    print("v do_move_vertical", row, col, "next", nx_row, nx_col)
    if field[nx_row][nx_col] == '.':
        print("v next is empty, so move")
        # simple move
        field[nx_row][nx_col] = '@'
        field[row][col] = '.'
        return (nx_row, nx_col)
    print("v next is not empty")
    if field[nx_row][nx_col] == '#':
        print("v it's a # so abort mission")
        return (row, col)
    print("v next is actually a ", field[nx_row][nx_col])

    next_box = find_next_box(field, nx_row, nx_col, d)
    boxes = [next_box]
    can_move = find_boxes(field, boxes, d)
    if can_move:
        for b in reversed(boxes):
            move_box_vertical(field, d, b)
        field[nx_row][col] = "@"
        field[row][col] = "."
        return (nx_row, col)
    else:
        return (row, col)

def do_move(field, row, col, m):
    d = dirs[m]
    if d[0] == 0:
        return do_move_horizontal(field, row, col, d[1])
    else:
        return do_move_vertical(field, row, col, d[0])

def print_field(field):
    for r in field:
        print("".join(r))
        
def score(field):
    s = 0
    for row_ix, row in enumerate(field):
        for col_ix, col in enumerate(row):
            if field[row_ix][col_ix] == '[':
                w1 = col_ix
                w2 = 9999999# len(row) - col_ix -1
                h1 = row_ix
                h2 = 9999999# len(field) - row_ix - 1
                s += 100 * min(h1, h2) + min(w1, w2)
    return s

with open(sys.argv[1]) as f:
    parse_field = True
    field = []
    moves = []
    for l in f.read().splitlines():
        if parse_field:
            if len(l) == 0:
                parse_field = False
            else:
                row = []
                for s in l:
                    if s == '#':
                        row.extend(['#','#'])
                    elif s == '@':
                        row.extend(['@', '.'])
                    elif s == '.':
                        row.extend(['.', '.'])
                    elif s == 'O':
                        row.extend(['[', ']'])
                field.append(row)
        else:
            moves.extend(l)

    (row, col) = find_at(field)
    print("row", row, "col", col)
    print_field(field)
    for m in moves:
        print(m)
        (row, col) = do_move(field, row, col, m)
        print_field(field)

    print(score(field))
