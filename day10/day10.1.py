import sys

DIRS = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]

def find_score(head_row, head_col, lines,  nines):
    print(head_row, head_col)
    altitude = lines[head_row][head_col]
    if altitude == 9:
        nines.append( (head_row, head_col) )
        return
    width = len(lines[0])
    height = len(lines[0])

    for d in DIRS:
        next_row = head_row + d[0]
        next_col = head_col + d[1]
        if next_row >= 0 and next_row < height and next_col >= 0 and next_col < width and lines[next_row][next_col] == altitude + 1:
            find_score(next_row, next_col, lines, nines)

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
    nums = []
    for str_row in lines:
        num_row = []
        for s in str_row:
            num_row.append(int(s))
        nums.append(num_row)
    print(nums)
    total = 0
    for row_ix, row in enumerate(nums):
        for col_ix, c in enumerate(row):
            if c == 0:
                nines = []
                find_score(row_ix, col_ix, nums, nines)
                total += len(nines)
    print(total)
