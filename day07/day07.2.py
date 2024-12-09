import sys
from itertools import product
import operator

def has_operators(result, values):
    for ops in product( [0, 1, 2], repeat=len(values) - 1 ):
        r = values[0]
        for i, v in enumerate(values[1:]):
            op = ops[i]
            if op == 0:
                r = r + v
            elif op == 1:
                r = r * v
            elif op == 2:
                r = int(str(r) + str(v))
            else:
                raise Exception()
        if r == result:
            return True
    return False

with open(sys.argv[1]) as f:
    total = 0
    for l in f.read().splitlines():
        (str_result, str_vals) = l.split(': ')
        result = int(str_result)
        vals = [int(v) for v in str_vals.split(' ')]
        if has_operators(result, vals):
            total += result
    print(total)
