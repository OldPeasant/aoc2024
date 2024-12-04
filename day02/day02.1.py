
def is_safe(report):
    print(report)
    deltas = set()
    for i in range(len(report) - 1):
        deltas.add(report[i+1] - report[i])
    if min(deltas) > 0 and max(deltas) <= 3:
        print("Good")
        return True
    if min(deltas) >= -3 and max(deltas) < 0:
        print("Good")
        return True
    print("Bad", min(deltas), max(deltas))
    return False

with open("input.txt") as f:
    count_safe = 0
    for l in f.read().splitlines():
        report = list(int(n) for n in l.split(" "))
        if is_safe(report):
            count_safe += 1
    print(count_safe)
