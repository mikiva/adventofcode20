from collections import deque

#inp = 389125467
inp = 974618352
input = deque(int(x) for x in str(inp))


def rotate_mugs(curr, r, mugs):
    while True:
        if mugs[r] == curr:
            return mugs
        else:
            mugs.rotate(1)


def play(mugs, rounds):
    c = 0
    put_aside = []
    current = mugs[c]
    for r in range(rounds):
        idx = mugs.index(current)
        c = idx
        for _ in range(3):
            put_aside.append(mugs[(idx+1) % len(mugs)])
            mugs.remove(mugs[(idx+1) % len(mugs)])
        target = None
        found = False
        diff = 1
        while not found:
            ch = idx
            for _ in range(len(mugs)):
                ch = (ch+1) % len(mugs)
                next = mugs[ch]
                if current - diff == next:
                    found = True
                    target = next
                    break
                elif current - diff < min(mugs):
                    found = True
                    target = max(mugs)
                    break

            diff += 1
        current = mugs[(idx+1) % len(mugs)]

        nm = mugs
        put_aside.reverse()
        for l in put_aside:
            nm.insert(nm.index(target) + 1 % len(nm), l)
        put_aside.clear()
        mugs = nm
        c = (c+1) % len(mugs)
        mugs = rotate_mugs(current, idx, mugs)
    return mugs


def part_1():
    rounds = 100
    p = play(input, rounds)
    idx = p.index(1)
    ans = []
    for _ in range(len(p)):
        ans.append(p[idx % len(p)])
        idx += 1
    mugs = rotate_mugs(1, 0, p)
    mugs = filter(lambda x: x != 1, mugs)
    mugs_str = "".join(map(str, mugs))
    return mugs_str


def solve():
    print(f'A: {part_1()}')


if __name__ == "__main__":
    solve()
