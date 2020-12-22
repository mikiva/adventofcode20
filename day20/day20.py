from collections import Counter, defaultdict

def flip_edge(edge):
    e = "".join(edge)
    return min(e, e[::-1])

def read_input(filename):
    tiles = defaultdict(str)
    with open(filename) as inp:
        for t in inp.read().split("\n\n"):
            id = t.split("\n")[0][-5:-1]
            tile = [x for x in t.split("\n")[1:]]
            tiles[id] = tile
    return tiles


#Assume all borders only appear once
def count_edges(tt):
    edges = Counter()
    product = 1
    for s in range(2):
        for t in tt:

            edge = [
                flip_edge(tt[t][0]),
                flip_edge([x[-1] for x in tt[t]]),
                flip_edge(tt[t][-1]),
                flip_edge([x[0] for x in tt[t]]),
            ]
            if s == 0:
                for e in edge:
                    edges[e] += 1
            else:
                if sum(1 for ed in edge if edges[ed] == 1) == 2:
                    product *= int(t)
    return product



def solve(filename):
    tiles = read_input(filename)

    print(f'A: {count_edges(tiles)}')



if __name__ == "__main__":
    solve("input")