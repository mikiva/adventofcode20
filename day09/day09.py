from itertools import combinations
preamble = 25
lines = []
with open("input.txt") as inp:
    lines = [int(x) for x in inp.read().split()]

def check_sum(pre, check, terms):
    for term in terms:
        if term < 2: continue
        for c in combinations(pre, term):
            if sum(c) == check:
                return True

    return False

invalid = -1
for l in range(preamble, len(lines)):
    pre, line = lines[l-preamble:l], lines[l]
    valid= check_sum(pre, lines[l], [2])
    if not valid:
        invalid = line
        mi, ma = min(pre), max(pre)
        break

def find_weakness(pre, check):
    weaklist = []
    for p in pre:
        weaklist.append(p)
        if sum(weaklist) == check:
            return True,  weaklist
    return False,weaklist

weakness = -1
for l in range(preamble, len(lines)):
    pre = lines[l-preamble:l]
    found , weak = find_weakness(pre, invalid)
    if found > 0:
        weakness = min(weak) + max(weak)
        break


print("a", invalid)
print("b", weakness)