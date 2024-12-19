import sys

impossible = set()

def is_possible(available, pattern):
    if len(pattern) == 0:
        return True
    if pattern in impossible:
        return False
    #print("  check is possible", pattern)
    for a in available:
        assert len(a) > 0
        if len(pattern) >= len(a) and pattern.startswith(a):
            #print("  we pick", a)
            if is_possible(available, pattern[len(a):]):
                return True
    #print("  nothing matched")
    impossible.add(pattern)
    return False

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
    available = lines[0].split(', ')
    count = 0
    for l in lines[2:]:
        if is_possible(available, l):
            print(l, "is possible")
            count += 1
        else:
            print(l, "is not possible")
    print("Total possible", count)
