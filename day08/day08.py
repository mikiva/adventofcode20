from collections import namedtuple
from time import sleep

codes = list()
Code = namedtuple('Code', ['visited', 'op', 'val'])


with open("input.txt", "r") as inp:
    for line in [x.split() for x in inp.readlines()]:
        codes.append(Code(False, line[0],int(line[1])))

def a(instructions):
    codes = instructions.copy()
    acc, loc = 0, 0
    exits = False
    while True:
        if loc >= len(temp):
            exits = True
            break
        code = codes[loc]
        
        if code.visited:
            break

        codes[loc] = code._replace(visited = True)
        op, val = code.op, code.val
        if op == "nop":
            loc += 1
        elif op == "jmp":
            loc += val
        elif op == "acc":
            acc += val
            loc += 1
    return exits, acc

def change(op):
    return 'jmp' if op == 'nop' else 'nop'

def b():
    for i in range(len(codes)):
        data = codes.copy()
        op = data[i].op
        if op in ['jmp', 'nop']: 
            data[i] = data[i]._replace(op = change(op))
        else:
            continue
        exits, acc = a(data)
        if exits: 
            return acc






    

temp= codes


print("a", a(temp)[1])
print("b", b())
