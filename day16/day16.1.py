import sys

sys.setrecursionlimit(5000)

dirs = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]

def is_opposite_dir(d1, d2):
    return d1[0] + d2[0] == 0 and d1[1] + d2[1] == 0

class ScoreCounter:
    def __init__(self):
        self.steps = 0
        self.turns = 0

    def score(self):
        return self.steps + 1000 * self.turns

def find_target(field, row, col, d, visited, score_counter):
    #print("find_target", row, col, d)
    #print(len(visited))
    best = None
    for next_dir in dirs:
        if not is_opposite_dir(next_dir, d):
            if next_dir != d:
                score_counter.turns += 1
            score_counter.steps += 1
            nr = row + next_dir[0]
            nc = col + next_dir[1]
            c = field[nr][nc]
            if c == 'E':
                print("found score", "steps", score_counter.steps, "turns", score_counter.turns)
                s = score_counter.score()
                if next_dir != d:
                    score_counter.turns -= 1
                score_counter.steps -= 1
                return s
            if ((nr, nc) not in visited or visited[(nr, nc)] > score_counter.score()) and c == '.':
                visited[(nr, nc)] = score_counter.score()
                v = find_target(field, nr, nc, next_dir, visited, score_counter)
                #del visited[(nr, nc)]
                if v is not None:
                    if best is None or  v < best:
                        best = v
            if next_dir != d:
                score_counter.turns -= 1
            score_counter.steps -= 1
    return best

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

    for row_ix, row in enumerate(lines):
        for col_ix, col in enumerate(row):
            if col == 'S':
                r = row_ix
                c = col_ix

    total = find_target(lines, r, c, (0, 1), {}, ScoreCounter())
    print(total)


