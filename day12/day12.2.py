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

def count_hori(pieces):
    by_row = {}
    for p in pieces:
        if p[0] not in by_row:
            s = set()
            by_row[p[0]] = s
        else:
            s = by_row[p[0]]
        s.add(p[1])
    total = 0
    for r, cols in by_row.items():
        sc = sorted(cols)
        print("row ", r, sc)
        count = 0
        prev = -99999999
        for s in sc:
            if s - prev > 1:
                count += 1
            else:
                total += count
                count = 0
            prev = s
        total += count
    print("totoal hori", total)
    return total

def count_vert(pieces):
    by_col = {}
    for p in pieces:
        if p[1] not in by_col:
            s = set()
            by_col[p[1]] = s
        else:
            s = by_col[p[1]]
        s.add(p[0])
    total = 0
    for c, rows in by_col.items():
        sr = sorted(rows)
        print("col ", c, sr)
        count = 0
        prev = -99999999
        for s in sr:
            if s - prev > 1:
                count += 1
            else:
                total += count
                count = 0
            prev = s
        total += count
    print("totoal vert", total)
    return total

def calc_border_len(region):
    vert_pieces = set()
    hori_pieces = set()
    for r in region:
        for d in [-1, 1]:
            if (r[0] + d, r[1]) not in region:
                hori_pieces.add( (r[0] + 0.1 * d, r[1]) )
            if (r[0], r[1] + d) not in region:
                vert_pieces.add( (r[0], r[1] + 0.1 * d) )
    print("Border pieces horizontal")
    print(hori_pieces)
    print("Border pieces vertical")
    print(vert_pieces)
    ch = count_hori(hori_pieces)
    cv = count_vert(vert_pieces)
    print("count hori", ch, "count vert", cv)
    return ch + cv

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
        
