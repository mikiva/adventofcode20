
def value_plus_mask(val, mask):
    val = [x for x in str(val)]
    for idx, m in enumerate(mask):
        if m != "X":
            val[idx] = m
    val = "".join(val)

    return val

def read_input():
    prog = {}
    mask = ""
    with open("input.txt") as inp:
        for line in inp:
            if line.startswith("mask"):
                mask = line.replace(" ", "").split("=")[1].strip("\n")
            else:
                key, value = line.replace(" ", "").split("=")
                value = "%036d" % int(bin(int(value))[2:])
                
                value = value_plus_mask(value, mask)
                
                prog[key] = value
    count = 0
    for v,k in prog.items():
        count += int(k,2)
    
    print(f'A: {count}')

def solve():
    read_input()



if __name__ == "__main__":
    solve()
    