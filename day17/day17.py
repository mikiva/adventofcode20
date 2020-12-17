from collections import defaultdict

def read_input():
    
    #input=".#.\n..#\n###"
    input = open("input").read()
    grid = []
    for row in input.split("\n"):
        r = []
        for cell in row:
            r.append(cell)
        grid.append(r)
    return grid

def parse_lines(grid):
    active = set()

    for i,v in enumerate(grid):
        for ii,vv in enumerate(v):
            if vv == "#":
                active.add((i,ii, 0))

    return active


def cycle(active):

    new_active = defaultdict(int)

    for x,y,z in active:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dz in [-1, 0, 1]:
                    if dx == 0 and dy == 0 and dz == 0:
                        continue
                    new_active[(x+dx, y+dy, z+dz)] += 1

    current_active = {p for p, v in new_active.items() if v == 3 or (v == 2 and p in active) }
    return current_active

def part_1(lines):
    for i in range(6):
        lines = cycle(lines)
    return len(lines)

def solve(lines):
    print(f'A: {part_1(lines)}')

if __name__ == "__main__":
    lines = parse_lines(read_input())

    solve(lines)


