import sys

def p_order(updates, orders):
    possible_indexes = {}
    for u in updates:
        possible_indexes[u] = list(range(len(updates)))

    while True:
        for k, v in possible_indexes.items():
            print(k, v)
        print()
        for o in orders:
            print("order", o)
            print(possible_indexes[o[0]])
            ix_low = max(possible_indexes[o[0]])
            possible_indexes[o[1]] =[ ix for ix in possible_indexes[o[1]] if ix > ix_low]
            print(possible_indexes[o[1]])
            ix_high = min(possible_indexes[o[1]])
            possible_indexes[o[0]] = [ix for ix in possible_indexes[o[0]] if ix < ix_high]
        max_len = max(len(pi) for pi in possible_indexes.values())
        if max_len == 1:
            result = []
            for u in updates:
                result.append(possible_indexes[u][0])
            return result

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    order = []
    
    updates = []
    in_orders = True
    for l in lines:
        if not l:
            in_orders = False
        else:
            #print(l)
            if in_orders:
                order.append([int(n) for n in l.split('|')])
            else:
                updates.append([int(n) for n in l.split(',')])

    s = 0
    for u in updates:
        update_set = set(u)
        relevant_orders = []
        for o in order:
            if o[0] in update_set and o[1] in update_set:
                relevant_orders.append(o)
        ok = True
        for r in relevant_orders:
            if u.index(r[0]) > u.index(r[1]):
                ok = False
                break
        if not ok:
            print(u)
            print(relevant_orders)
            v = p_order(u, relevant_orders)
            s += v[len(v)//2]
    print(s)

