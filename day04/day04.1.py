import sys


with open(sys.argv[1]) as f:
    rows = f.read().splitlines()
    count = 0
    for row in rows:
        for col in range(0, len(row) - 3):
            s = row[col:col+4]
            if s == 'XMAS' or s == 'SAMX':
                count += 1
                print("yes", s)
            else:
                print("no", s)
        print()
    print("-------")
    for col in range(len(rows[0])):
        for row in range(len(rows) - 3):
            s = ""
            for i in range(4):
                #print("ix:", row, i, col)
                s += rows[row+i][col]
            print(s)
            if s == 'XMAS' or s == 'SAMX':
                count += 1
        print()
    print("-------")
    for col in range(len(rows[0]) - 3):
        for row in range(len(rows) - 3):
            s = ""
            for i in range(4):
                #print("ix:", row, i, col)
                s += rows[row+i][col+i]
            print(s)
            if s == 'XMAS' or s == 'SAMX':
                count += 1
        print()
    print("-------")
    for col in range(len(rows[0]) - 3):
        for row in range(3, len(rows)):
            s = ""
            for i in range(4):
                #print("ix:", row, i, col)
                s += rows[row-i][col+i]
            print(s)
            if s == 'XMAS' or s == 'SAMX':
                count += 1
        print()
    print(count)
