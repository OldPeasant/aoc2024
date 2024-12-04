

with open("input.txt") as f:
    lines = f.read().splitlines()
    left = []
    right = []
    for l in lines:
        parts = l.split(" ")
        left.append(int(parts[0]))
        right.append(int(parts[-1]))
    left.sort()
    right.sort()
    sum = 0
    for i in range(len(left)):
        sum += abs(right[i]-left[i])
    print(sum)
