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

def get_abas(address):
    abas = [''.join((address[i],address[i+1],address[i+2])) for i in range(0,len(address)-2) if address[i] == address[i+2]]
    return abas

def supported(address):
    if has_abba(filter_hypernet(address)) and not has_abba(filter_non_hypernet(address)):
        return True
    else:
        return False

def supported_aba(address):
    abas = get_abas(filter_hypernet(address))
    for aba in abas:
        bab = invert_aba(aba)
        if filter_non_hypernet(address).find(bab) >= 0:
            return True
    return False

def invert_aba(aba):
    return ''.join((aba[1],aba[0],aba[1]))

p1 = len([a for a in data if supported(a)])
print(f"Part one: {p1}")

p2 = len([a for a in data if supported_aba(a)])
print(f"Part two: {p2}")
