start = [7,14,0,17,11,1,2]
#start = [0,3,6]




def play(max_turns):

    #spoken = {}

    turn, current, spoken = 0, 0, []
    for s in start:
        turn += 1
        current = s
        spoken.append(s)

    while 1 == 1:
        turn += 1
        
        if turn > max_turns:
            break
        if spoken.count(current) > 1:
            idx1 = -1
            idx2 = -1
            occ = (i+1 for i,n in enumerate(spoken) if n == current)

            idxs = []
            while 1 == 1:
                try:
                    idxs.append(next(occ))
                except StopIteration:
                    break
            current = idxs[-1] - idxs[-2]
            
        
        else:
            current = 0
        
        spoken.append(current)
        if turn % 10000 == 0:
            print(turn, current)
    return current
            

def solve():    
    print(f'A: {play(2020)}')
    #print(f'B: {play(30000000)}')





if __name__ == "__main__":
    solve()