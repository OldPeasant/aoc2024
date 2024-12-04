import sys


def check(sub):
    if sub[1][1] != 'A':
        return False
    s1 = set()
    s2 = set()
    s1.add(sub[0][0])
    s1.add(sub[2][2])
    s2.add(sub[2][0])
    s2.add(sub[0][2])
    if 'M' in s1 and 'S' in s1 and 'M' in s2 and 'S' in s2:
        return True
    return False

with open(sys.argv[1]) as f:
    rows = f.read().splitlines()
    count = 0
    for row_ix in range(len(rows)-2):
        for col_ix in range(len(rows) - 2):
            sub = []
            sub.append(rows[row_ix][col_ix:col_ix + 3])
            sub.append(rows[row_ix+1][col_ix:col_ix + 3])
            sub.append(rows[row_ix+2][col_ix:col_ix + 3])
            if check(sub):
                count += 1
                print("yes", sub)
            else:
                print("no", sub)
        print()
    print(count)
