import re
def read_input(file):
    lines = open(file).read().split("\n")
    return lines

def calculate_items(a,b, op = "+"):

    if op == "*":
        if a == 0:
            a = 1
        return a * b
    elif op == "+":
        return a + b


def calculate_line(line, op = "+"):
    current = 0    
    current_op = op
    for idx, item in enumerate(line):
        if item == "+" or item == "*":
            current_op = item
        else:
            current = calculate_items(current, int(item), current_op)

    return current


def calc(line, part):
    
    if part == 1:
        tot = 0
        op = "+"
        if len(line.split()) == 1:
            return int(line)
        for item in line.split():
            if item == "*" or item == "+":
                op = item
            else:
                tot = calculate_items(tot, int(item), op)

    return tot


def get_parenthesis(line, part):
    openp, closep = 0, 0
    ind, out = 0,0
    for i,v in  enumerate(line):
        if v == "(":
            openp += 1
            if openp == 1:
                ind = i+1
        elif v == ")":
            closep += 1
            if openp == closep:
                out = i
                break
            
    if openp == 0:
        return calc(line, part), line

    new_line = line[:ind-1] + str(get_parenthesis(line[ind:out], part)[0]) + line[out+1:]
    return get_parenthesis(new_line, part)
            
def part_1(lines):
    sums = 0
    for line in lines:
        tots, l = get_parenthesis(line, 1)
        sums += tots

    return sums


def solve():
    lines = read_input("input")
    print(f'A: {part_1(lines)}')

if __name__ == "__main__":

    solve()
