from collections import namedtuple
from copy import deepcopy
orig = [list(x.strip("\n")) for x in  open("input.txt")]


grid = deepcopy(orig)

def check_neigh(r, c, temp):
    if temp[r][c] == "L":
        for cr in [1, 0, -1]:
            for cc in [1,0,-1] :
                if r+cr < 0 or c+cc < 0: continue
                try:
                    if cr == 0 and cc == 0: 
                        continue
                    elif temp[r+cr][c+cc] == "#":
                        return "L"
                except:
                    continue
        return "#"
    elif temp[r][c] == "#":
        count = 0
        for cr in [1, 0, -1]:
            for cc in [1,0,-1] :
                if r+cr < 0 or c+cc < 0: continue
                try:
                    if cr == 0 and cc == 0: 
                        continue
                    elif temp[r+cr][c+cc] == "#": 
                        count = count+1
                except:
                    continue
        if count > 3: 
            return "L"
        else: return "#"
    elif temp[r][c] == ".": return "."
    

def compare(a,b):
    for row in range(len(a)):
        if a[row] != b[row]: return False
    return True

def a():
    rows = len(orig)
    cols = len(orig[0])
    
    current = deepcopy(orig)
    while True:
        grid = deepcopy(current)
        for r in range(rows):
            for c in range(cols):
                grid[r][c] = check_neigh(r,c, current)

        if compare(current, grid):
            break
       
        current = deepcopy(grid)

    occupied = 0
    for row in current:
        for col in row:
            if col == "#": occupied += 1
        
    return occupied

def run():
    print(f'A: {a()}')



run()