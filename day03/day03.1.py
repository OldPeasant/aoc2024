import sys
import re

filename = sys.argv[1]

with open(filename) as f:
    text = f.read()

    a_string = "the quick brown fox jumps over the lazy dog. the quick brown fox jumps over the lazy dog"

    # Find all indices of 'the'
    #indices_object = re.finditer(pattern='mul\([0-9]{1, 3},[0-9]{1, 3}\)', string=text)
    indices_object = re.findall(pattern='mul\([0-9]{1,3},[0-9]{1,3}\)', string=text)
    sum = 0
    for i in indices_object:
        parts = i.split('(')[1].split(')')[0].split(',')
        print(parts)
        sum += int(parts[0]) * int(parts[1])
    print(sum)
    #indices = [index.start() for index in indices_object]
    #print(indices)
