from datetime import datetime
from itertools import combinations

preamble = 25
lines = [int(x) for x in open("input.txt")]


def check_sum(pre, check, terms):
    for c in combinations(pre, terms):
        if sum(c) == check:
            return True
    return False


def find_invalid():
    for l in range(preamble, len(lines)):
        pre, line = lines[l-preamble:l], lines[l]
        valid = check_sum(pre, lines[l], 2)
        if not valid:
            return line
    return -1


def try_weakness(pre, check):
    weaklist = []
    for p in pre:
        weaklist.append(p)
        if sum(weaklist) == check:
            return True,  weaklist
    return False, weaklist


def find_weakness(invalid):
    weakness = -1
    for l in range(preamble, len(lines)):
        pre = lines[l-preamble:l]
        found, weak = try_weakness(pre, invalid)
        if found > 0:
            weakness = min(weak) + max(weak)
            break

    return {"a": invalid, "b": weakness}


def run():
    print(f'{find_weakness(find_invalid())}')


start_time = datetime.now()
run()
end_time = datetime.now()
tot_time = (end_time - start_time).microseconds / 1000

print(f'Time: {tot_time} ms')
