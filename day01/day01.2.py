

def count_occ(lst, n):
    cnt = 0
    for l in lst:
        if l == n:
            cnt += 1
    return cnt

with open("input.txt") as f:
    lines = f.read().splitlines()
    left = []
    right = []
    for l in lines:
        parts = l.split(" ")
        left.append(int(parts[0]))
        right.append(int(parts[-1]))
    #left.sort()
    #right.sort()
    sum = 0
    for i in left:
        sum += i * count_occ(right, i)
    print(sum)
