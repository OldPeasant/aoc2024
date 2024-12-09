import sys

def find_gap(blocks, l):
    #print(f"search gap of {l}")
    i = 0
    while True:
        if blocks[i] == '.':
            j = i
            while j < len(blocks) and blocks[j] == '.':
                j += 1
            
            #print(f"  dots at {i}..{j}") 
            if j - i  >= l:
                return i
            i = j
        i += 1
        if i > len(blocks) - 1:
            return -1


with open(sys.argv[1]) as f:
    diskmap = f.read().splitlines()[0]
    ix = 0
    blocks = []
    space = False
    for d in diskmap:
        l = int(d)
        for i in range(l):
            if space:
                blocks.append('.')
            else:
                blocks.append(ix)
        if space:
            space = False
        else:
            ix += 1
            space = True
    #print("".join(str(b) for b in blocks))
    ix_to = len(blocks) - 1
    ix_from = ix_to
    while True:
        while blocks[ix_from] == '.':
            ix_from -= 1
        ix_to = ix_from
        while blocks[ix_to] == blocks[ix_from] and ix_from >= 0:
            ix_from -= 1
        #print(f"block {ix_from} {ix_to}")

        ix_gap = find_gap(blocks, ix_to - ix_from)
        #print(f"gap {ix_gap}")
        if ix_gap >= 0 and ix_gap < ix_from:
            for i in range(ix_to - ix_from):
                #print("shifting", i, ix_from, ix_to)
                blocks[ix_gap + i] = blocks[ix_from + i + 1]
                blocks[ix_from + i + 1] = '.'
        ix_to = ix_from
        if ix_from < 0:
            break
        #print("".join(str(b) for b in blocks))
    #print("".join(str(b) for b in blocks))
    cs = 0
    i = 0
    v = 0
    prev = -1
    for b in blocks:
        if b != '.':
            cs += i * b
        i += 1
    print(cs)
