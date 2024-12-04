
def is_safe(report):
    deltas = set()
    for i in range(len(report) - 1):
        deltas.add(report[i+1] - report[i])
    if min(deltas) > 0 and max(deltas) <= 3:
        return True
    if min(deltas) >= -3 and max(deltas) < 0:
        return True
    return False

def has_safe_subset(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        sub_report = []
        sub_report.extend(report[:i])
        sub_report.extend(report[i + 1:])
        if is_safe(sub_report):
            return True
    return False

with open("input-dummy.txt") as f:
    count_safe = 0
    for l in f.read().splitlines():
        report = list(int(n) for n in l.split(" "))
        if has_safe_subset(report):
            count_safe += 1
    print(count_safe)
