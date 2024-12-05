import sys

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    order = []
    
    updates = []
    in_orders = True
    for l in lines:
        if not l:
            in_orders = False
        else:
            print(l)
            if in_orders:
                order.append([int(n) for n in l.split('|')])
            else:
                updates.append([int(n) for n in l.split(',')])

    s = 0
    for u in updates:
        update_set = set(u)
        all_ok = True
        for o in order:
            if o[0] in update_set and o[1] in update_set:
                if u.index(o[0]) >= u.index(o[1]):
                    all_ok = False
        if all_ok:
            s += u[len(u)//2]
    print(s)

