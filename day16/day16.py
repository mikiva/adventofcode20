import re
data = ""
with open("input") as inp:
    data = inp.read()



def parse_valid_fields(data):   
    valid = set()
    valid_part = data.split("\n\n")[0]
    matcher = re.compile("([0-9]+-[0-9]+)")
    vals = re.findall(matcher, valid_part)
    for val in vals:
        low, high = val.split("-")
        for v in range(int(low), int(high)+1):
            valid.add(v)

    return valid


def parse_nearby_tickets(data):
    valid_part = data.split("\n\n")[2]
    ticket_numbers = valid_part.split("\n")[1:]
    numbers = []
    tickets = []
    for ticket in ticket_numbers:
        tick = []
        for number in [int(x) for x in ticket.split(",")]:
            tick.append(number)
        tickets.append(tick)


    return tickets

def find_invalid_numbers(valid, tickets):
    invalid =[]
    for tick in tickets:
        invalid.extend([x for x in tick if x not in valid])

    return invalid

def solve_part_1():
    valid = parse_valid_fields(data)
    nearby_tickets = parse_nearby_tickets(data)
    invalid = find_invalid_numbers(valid, nearby_tickets)
    return sum(invalid)


def solve():
    print(f'A: {solve_part_1()}')




if __name__ == "__main__":
    solve()