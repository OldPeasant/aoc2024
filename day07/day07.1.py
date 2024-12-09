import sys
from itertools import combinations
import operator

def has_operators(result, values):
    print("Values:", values)
    for bits in range(pow(2, len(values) - 1)):
        ops = []
        for j in range(len(values)-1):
            ops.append( True if (bits & pow(2, j)) else False )
        print(ops)
        r = values[0]
        for i, v in enumerate(values[1:]):
            op = ops[i]
            if op:
                r = r + v
            else:
                r = r * v
            print(op)
        if r == result:
            print("yes")
            return True
        else:
            print("No")
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
