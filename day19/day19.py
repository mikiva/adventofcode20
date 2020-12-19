import re

def read_input(file):
    rules, messages = open(file).read().split("\n\n")

    mess = []
    rule_list = dict()

    for rule in rules.split("\n"):
        id, content = rule.split(":")
        rule_list[id] = content.strip().split()
    for message in messages.split("\n"):
        mess.append(message)
    return rule_list, mess


def get_regex_part(part, rules):
    if part.startswith('"'):
        return part[1]
    elif part == '|':
        return '|'
    else: 
        return '(' + build_regexp(part, rules) + ')'

def build_regexp(number, rules):
    return ''.join(get_regex_part(reg, rules) for reg in rules[number])


def part_1(messages, rules):

    regexp = build_regexp('0', rules)
    count = 0
    for message in messages:
        if re.match('^' + regexp + '$', message):
            count += 1
    return count

def solve(file):
    rules, messages = read_input(file)
    print(f'A: {part_1(messages, rules)}')

if __name__ == "__main__":
    solve("input")