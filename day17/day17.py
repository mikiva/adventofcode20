import numpy as np

from collections import defaultdict

def read_input():
    
    input=".#.\n..#\n###"
    #input = open("input").read()
    #with open("input") as inp:
    #    input = inp.read()
    print(input)

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

    print(active)
    return active







if __name__ == "__main__":
    lines = parse_lines(read_input())
    #print(lines)
   # print(part1(grid))
    print(lines)
    pass


"""
Lägg in alla aktiva i ett set. 
För varje cykel, kolla alla aktiva och titta på varje granne med nästlade for-loopar, räkna hur många av dessa som återfinns i befintligt set.
Lägg till varje punkt i nytt set.
Returnera endast de punkter som har grannar enligt reglerna

"""