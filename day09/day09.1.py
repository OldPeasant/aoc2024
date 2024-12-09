import sys

def find_first_dot(blocks):
    i = 0
    while True:
        if blocks[i] == '.':
            return i
        i += 1
def find_last_non_dot(blocks):
    i = len(blocks) - 1
    while True:
        if blocks[i] != '.':
            return i
        i -= 1

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
    while True:
        last_non_dot = find_last_non_dot(blocks)
        first_dot = find_first_dot(blocks)
        if first_dot > last_non_dot:
            break
        blocks[first_dot] = blocks[last_non_dot]
        blocks[last_non_dot] = '.'

        #print("".join(str(b) for b in blocks))
    #print("".join(str(b) for b in blocks))
    cs = 0
    for i, b in enumerate(blocks):
        if b == '.':
            break
        cs += i * b
    print(cs)
