import sys

dirs = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]

def flood(plan, region, rx, cx, c):
    region.add( (rx, cx) )
    for d in dirs:
        np = (rx + d[0], cx + d[1])
        if np in region:
            continue
        nc = plan[np[0]][np[1]]
        if nc == c:
            region.add(np)
            flood(plan, region, np[0], np[1], c)
        
def calc_border_len(region):
    total = 0
    for r in region:
        for d in dirs:
            if (r[0] + d[0], r[1] + d[1]) not in region:
                total += 1
    return total

def process_region(plan, rx, cx):
    c = plan[rx][cx]
    region = set()
    flood(plan, region, rx, cx, c)
    border_len = calc_border_len(region)
    price = len(region) * border_len
    print("flooded", c, len(region), border_len, price)
    for rx, row in enumerate(plan):
        row_str = ""
        for cx, col in enumerate(row):
            #if (rx, cx) in border:
            #    row_str += "$"
            if (rx, cx) in region:
                row_str += "*"
            else:
                row_str += col
        print(row_str)
    for b in region:
        plan[b[0]][b[1]] = '.'
    return price

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
    
    bw = len(lines[0]) + 2
    bh = len(lines) + 2
    wb = []
    wb.append( list('.' * bw))
    for l in lines:
        bl = []
        bl.append('.')
        bl.extend(list(l))
        bl.append('.')
        wb.append(bl)
    wb.append( list('.' * bw))
    
    for l in wb:
        print("".join(l))

    total = 0
    for row_ix, row in enumerate(wb):
        for col_ix, c in enumerate(row):
            if c != '.':
                price = process_region(wb, row_ix, col_ix)
                print('price of region', c, price)
                total += price
    print(total)
        
