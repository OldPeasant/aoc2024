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

def do_move(field, row, col, m):
    d = dirs[m]
    nx_row = row + d[0]
    nx_col = col + d[1]
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
    while field[nx_row][nx_col] == 'O':
        print("next is O")
        nx_row += d[0]
        nx_col += d[1]
    if field[nx_row][nx_col] == '#':
        print("bumped into #")
        return (row, col)
    print("This should be a dot", field[nx_row][nx_col])
    field[nx_row][nx_col] = 'O'
    field[row][col] = '.'
    field[row + d[0]][col + d[1]] = '@'
    return ( row + d[0], col + d[1])

def print_field(field):
    for r in field:
        print("".join(r))
        
def score(field):
    s = 0
    for row_ix, row in enumerate(field):
        for col_ix, col in enumerate(row):
            if field[row_ix][col_ix] == 'O':
                s += 100 * row_ix + col_ix
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
                field.append( [s for s in l] )
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
