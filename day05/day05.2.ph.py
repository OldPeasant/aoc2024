import sys

def p_order(updates, orders):
    up = list(updates)
    while True:
        changed = False
        for o in orders:
            ix1 = up.index(o[0])
            ix2 = up.index(o[1])
            if ix1 > ix2:
                new_up = []
                new_up.extend(up[:ix2])
                new_up.extend(up[ix2 + 1:ix1+1])
                new_up.append(up[ix2])
                new_up.extend(up[ix1+1:])
                up = new_up
                changed = True
                break
        if not changed:
            return up

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    order = []
    
    updates = []
    in_orders = True
    for l in lines:
        if not l:
            in_orders = False
        else:
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
            v = p_order(u, relevant_orders)
            s += v[len(v)//2]
    print(s)

