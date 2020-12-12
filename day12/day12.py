instr = []
with open("input.txt") as inp:
    for line in inp:
        instr.append((line[0], int(line[1:])))

dirs = ["N", "E", "S", "W"]
wp = [-1,10]
pox, poy = 0,0
direction = "E"
def full_turn():
    global direction
    if direction == "E":
        direction = "W"
    elif direction == "W":
        direction = "E"
    elif direction == "S":
        direction = "N"
    elif direction == "N":
        direction = "S"

def turn(dir, deg):
    global direction


    if deg == 180:
        full_turn()
    elif deg == 270:
        full_turn()
        turn(dir, deg-180)
    else:
        if dir == "L":
            if direction == "N":
                direction = "W"
            elif direction == "W":
                direction = "S"
            elif direction == "S":
                direction = "E"
            elif direction == "E":
                direction = "N"
        elif dir == "R":
            if direction == "N":
                direction = "E"
            elif direction == "E":
                direction = "S"
            elif direction == "S":
                direction = "W"
            elif direction == "W":
                direction = "N"
def move_dir(dir, dist):
    global pox, poy, direction

    if dir == "N":
        poy -= dist
    elif dir == "S":
        poy += dist
    elif dir == "W":
        pox -= dist
    elif dir == "E":
        pox += dist
    elif dir == "F":
        move(direction, dist)


def move(dir, dist):
    if dir in ["L", "R"]:
        turn(dir, dist)
    else:
        move_dir(dir, dist)


def move_wp(dir, dist):
    global wp

    if dir == "N":
        wp[0] -= dist
    elif dir == "S":
        wp[0] += dist
    elif dir == "W":
        wp[1] -= dist
    elif dir == "E":
        wp[1] += dist


def a():
    for ins in instr:
        dir, dist = ins[0], ins[1]
        move(dir, dist)

    return abs(pox) + abs(poy)


def turn_wp(dir, deg):
    global wp
    degrees = deg
    if dir == "R":
        degrees = 360 - deg
    for turn in range(degrees//90 % 4):
        wp = [-wp[1], wp[0]]

def move_ship(dist):
    global poy, pox, wp
    pox += wp[0] * dist
    poy += wp[1] * dist

def b():
    global poy, pox
    for ins in instr:
        dir, dist = ins[0], ins[1]

        if dir in ["L", "R"]:
            turn_wp(dir, dist)
        elif dir in dirs:
            move_wp(dir, dist)
        else:
            move_ship(dist)

    return abs(poy) + abs(pox)





def run():
    global pox, poy
    poy, pox = 0,0
    print(f'A: {a()}')
    poy, pox = 0,0
    print(f'B: {b()}')

run()