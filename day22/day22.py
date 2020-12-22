
def read_input(filename):
    p1, p2 = open(filename).read().split("\n\n")
    p1 = [int(x) for x in p1.split("\n")[1:]]
    p2 = [int(x) for x in p2.split("\n")[1:]]
    return p1,p2


def play(p1, p2):

    while len(p1) > 0  and len(p2) > 0:
        p1play = p1.pop(0)
        p2play = p2.pop(0)

        if p1play > p2play:
            p1.append(p1play)
            p1.append(p2play)
        elif p1play < p2play:
            p2.append(p2play)
            p2.append(p1play)

    if len(p1) == 0:
        return p2
    return p2
 

def part_1(p1,p2):
    winner = play(p1,p2)
    count = 0
    for i,p in enumerate(winner[::-1]):
        count += p * (i +1)
    return count
def solve(filename):
    p1, p2 = read_input(filename)

    print(f'A: {part_1(p1,p2)}')


if __name__ == "__main__":
    solve("input")