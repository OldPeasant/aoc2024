import sys

def combo(reg, op):
    if op <= 3:
        return 3
    if op == 4:
        return reg.a
    if op == 5:
        return reg.b
    if op == 6:
        return reg.c
    raise Exception(f"Combo operand {op}")

def adv(prog, reg, pos, op):
    print("adv", reg, pos, op)
    numerator = reg.a
    denominator = pow(2, combo(reg, op))
    quot = int(numerator / denominator)
    reg.a = quot
    return pos + 2

def bxl(prog, reg, pos, op):
    print("bxl", reg, pos, op)
    bxor = reg.b ^ op
    reg.b = bxor
    return pos + 2

def bst(prog, reg, pos, op):
    print("bst", reg, pos, op)
    m = combo(reg, op) % 8
    reg.b = m
    return pos + 2

def jnz(prog, reg, pos, op):
    print("jnz", reg, pos, op)
    if reg.a == 0:
        return pos + 2
    else:
        return op

def bxc(prog, reg, pos, op):
    print("bxc", reg, pos, op)
    reg.b = reg.b ^ reg.c
    return pos + 2

def out(prog, reg, pos, op):
    print("out", combo(reg, op) % 8)
    return pos + 2

def bdv(prog, reg, pos, op):
    print("bdv", reg, pos, op)
    numerator = reg.a
    denominator = pow(2, combo(reg, op))
    quot = int(numerator / denominator)
    reg.b = quot
    return pos + 2

def cdv(prog, reg, pos, op):
    print("cdv", reg, pos, op)
    numerator = reg.a
    denominator = pow(2, combo(reg, op))
    quot = int(numerator / denominator)
    reg.c = quot
    return pos + 2

opcodes = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}
class Registers:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        return f"Registers[{self.a}, {self.b}, {self.c}]"

def run(prog, reg):
    pos = 0
    while pos < len(prog):
        instr = prog[pos]
        op = prog[pos + 1]
        print("instr", instr, "op", op, "pos", pos)
        pos = opcodes[instr](prog, reg, pos, op)
        #pos += 2
with open(sys.argv[1]) as f:

    lines = f.read().splitlines()
    reg = Registers(*( int(l.split(": ")[1]) for l in lines[:3]))
    prog = [int(s) for s in lines[4].split(": ")[1].split(",")]

    print("Registers", reg)
    print("Program", prog)

    run(prog, reg)
