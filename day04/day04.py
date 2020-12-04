

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
opt = "cid"

pp = []

with open("input.txt", "r") as inp:
    p = ""
    for line in inp:
        p  += line
    pp = p.split("\n\n")

def check_passport(passport):
    valid = True
    for f in fields:
        if f not in [x[:3] for x in passport.split()]:
            valid = False

    return valid

def byr(p):
    return int(p) >= 1920 and int(p) <= 2020

def iyr(p):
    return int(p) >= 2010 and int(p) <= 2020

def eyr(p):
    return int(p) >= 2020 and int(p) <= 2030
def hgt(p):
    if p[-2:] == "cm":
        return int(p[:3]) >= 150 and int(p[:3]) <= 193
    elif p[-2:] == "in":
        return int(p[:2]) >= 59 and int(p[:2]) <= 76
def hcl(p):
    if p.startswith("#") and len(p[1:]) == 6:
        color = int(p[1:], 16) #Throws if error
        return True
    return False
def ecl(p):
    return p in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
def pid(p):
    return len(str(p)) == 9 and int(p) #Throws if not integer



def check_passport_for_real(passport):
    valid = True
    for field in [x.split(":") for x in passport.split()]:
        try:
            if field[0] == "byr":
                valid = byr(field[1])
            elif field[0] == "iyr":
                valid = iyr(field[1])
            elif field[0] == "eyr":
                valid = eyr(field[1])
            elif field[0] == "hgt":
                valid = hgt(field[1])
            elif field[0] == "hcl":
                valid = hcl(field[1])
            elif field[0] == "ecl":
                valid = ecl(field[1])
            elif field[0] == "pid":
                valid = pid(field[1])
        except:
            valid = False
        if not valid:
            break
    return valid

valid = []
valid_for_real = []

for p in pp:
    p = p.replace("\n", " ")
    
    if check_passport(p):
        valid.append(p)
        if check_passport_for_real(p):
            valid_for_real.append(p)

print("a", len(valid))
print("b", len(valid_for_real))