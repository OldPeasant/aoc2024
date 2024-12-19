import sys

impossible = set()

class Counter:
    def __init__(self):
        self.count = 0

def is_possible(available, pattern, counter):
    if len(pattern) == 0:
        counter.count += 1
        return
    if pattern in impossible:
        return
    #print("  check is possible", pattern)
    has_possible = False
    for a in available:
        assert len(a) > 0
        if len(pattern) >= len(a) and pattern.startswith(a):
            has_possible = True
            #print("  we pick", a)
            is_possible(available, pattern[len(a):], counter)
    #print("  nothing matched")
    if not has_possible:
        impossible.add(pattern)

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
    available = lines[0].split(', ')
    count = 0
    for l in lines[2:]:
        print("check", l)
        counter = Counter()
        is_possible(available, l, counter)
        print(counter.count)
        count += counter.count
    print("Total possible", count)
