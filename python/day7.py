import re

with open('data/day7.input') as f:
    data = [e.strip() for e in f.readlines()]

def filter_hypernet(address):
    return re.sub("\[.*?\]", "-", address)

def filter_non_hypernet(address):
    pattern = r'\[([A-Za-z0-9]*)\]'
    return '-'.join(re.findall(pattern, address))

def has_abba(address):
    i = 0
    while i < len(address)-3:
        if address[i] == address[i+3] and address[i+1] == address[i+2] and address[i] != address[i+1]:
            return True
        i += 1

    return False

def supported(address):
    if has_abba(filter_hypernet(address)) and not has_abba(filter_non_hypernet(address)):
        print(f"good: {address}")
        return True
    else:
        # print(f"bad: {address}")
        return False

p1 = len([a for a in data if supported(a)])
print(f"Part one: {p1}")
