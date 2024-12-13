import sys

def parse_coords(c):
    print("parse_coords", c)
    return int(c.split("+")[1])

def parse_target(c):
    print("parse_target", c)
    return 10000000000000 + int(c.split("=")[1])
    #return int(c.split("=")[1])

def parse_button(btn):
    coords = btn.split(": ")[1]
    return [parse_coords(c) for c in coords.split(", ")]

def parse_prize(p):
    coords = p.split(": ")[1]
    return [parse_target(c) for c in coords.split(", ")]

def needed_tokens(btn_a, btn_b, prize):
    j = (prize[1] * btn_a[0] - prize[0] * btn_a[1]) / (btn_b[1] * btn_a[0] - btn_b[0] * btn_a[1])
    i = (prize[0] - j * btn_b[0]) / btn_a[0]
    print("i", i, "j", j)
    print("match?", prize, i * btn_a[0] + j * btn_b[0], i * btn_a[1] + j * btn_b[1]) 
    if i == int(i) and j == int(j):
        return int(3 * i) + j
    else:
        return 0
    #best = None
    #print("Needed tokens", btn_a, btn_b, prize)
    #for i in range(100):
    #    ax = i * btn_a[0]
    #    ay = i * btn_a[1]
    #    j1 = (prize[0] - ax) / btn_b[0]
    #    j2 = (prize[1] - ay) / btn_b[1]
    #    if j1 == int(j1) and j2 == int(j2) and j1 == j2:
    #        t = 3 * i + j1
    #        if best is None or t < best:
    #            best = t
    #return best if best else 0

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
    ix = 0
    total = 0
    while ix < len(lines):
        btn_a = lines[ix]
        ix += 1
        btn_b = lines[ix]
        ix += 1
        prize = lines[ix]
        ix += 2
        tokens = needed_tokens(parse_button(btn_a), parse_button(btn_b), parse_prize(prize))
        total += tokens
    print(total)
