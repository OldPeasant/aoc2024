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
            print("possible", o[0], possible_indexes[o[0]])
            print("possible", o[1], possible_indexes[o[1]])

            ix_low = min(possible_indexes[o[0]])
            print("low", ix_low)
            ix_high = max(possible_indexes[o[1]])
            print("high", ix_high)
            print("---")

            possible_indexes[o[1]] = [i for i in possible_indexes[o[1]] if i > ix_low]
            possible_indexes[o[0]] = [i for i in possible_indexes[o[0]] if i < ix_high]

            for k, v in possible_indexes.items():
                print(k, v)
            print()

        max_len = max(len(pi) for pi in possible_indexes.values())
        if max_len == 1:
            result = []
            result = [(u, possible_indexes[u][0]) for u in updates]
            result.sort(key=lambda e:e[1])
            return [r[0] for r in result]

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
            print("Aus", u, "wird", v)
            s += v[len(v)//2]
    print(s)

