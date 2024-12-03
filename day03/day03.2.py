import sys
import re

filename = sys.argv[1]

def max_below(lst, i):
    m = -1
    for l in lst:
        if l < i:
            m = l
    return m

with open(filename) as f:
    text = f.read()

    a_string = "the quick brown fox jumps over the lazy dog. the quick brown fox jumps over the lazy dog"

    indexes_do = [i.span()[0] for i in re.finditer(pattern='do\(\)', string=text)]
    indexes_dont = [i.span()[0] for i in re.finditer(pattern='don\'t\(\)', string=text)]
    print(indexes_do)
    print(indexes_dont)
    indices_object = re.finditer(pattern='mul\([0-9]{1,3},[0-9]{1,3}\)', string=text)
    sum = 0
    for i in indices_object:
        s = i.span()
        m = text[s[0] : s[1]]
        last_do = max_below(indexes_do, s[0])
        last_dont = max_below(indexes_dont, s[1])
        if last_dont < 0 or last_do > last_dont:
            print('yes', m)
            parts = m.split('(')[1].split(')')[0].split(',')
        #print(parts)
            sum += int(parts[0]) * int(parts[1])
    print(sum)
    #indices = [index.start() for index in indices_object]
    #print(indices)
