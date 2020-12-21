from collections import defaultdict


def print_tiles(tiles):
    for tile in tiles:
        print(tile)
        for t in tiles[tile]:
            print("".join(t))
        print()

def print_tile(tile):
    for t in tile:
        print("".join(t))
    

def read_input(filename):

    tiles = defaultdict(int)
    with open(filename) as inp:
        for t in inp.read().split("\n\n"):
            id = int(t.split("\n")[0][-5:-1])
            tile = [list(x) for x in t.split("\n")[1:]]
            tiles[id] = tile

    return tiles



def get_edges(tt):

    for t in tt:

        edges = [
            "".join(tt[t][0]),
            "".join([x[-1] for x in tt[t]]),
            "".join(tt[t][-1]),
            "".join([x[0] for x in tt[t]]),
        ]

        print(edges)
        print()
        print(rotate(edges))
        print()
        print_tile(tt[t])
        print()

def rotate(edges):
    return edges[1:] + edges[:1]


def solve(filename):
    tiles = read_input(filename)
    #print_tiles(tiles)

    get_edges(tiles)


if __name__ == "__main__":
    solve("ex")