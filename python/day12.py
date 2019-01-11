from collections import defaultdict

with open('data/day12.input') as f:
    data = [e.strip() for e in f.readlines()]

def is_number(s):
    try:
        i = int(s)
        return True
    except (ValueError, TypeError):
        return False

reg = defaultdict(int)

i = 0
reg['c'] = 1
while i < len(data):
    cmd = data[i].split()

    if cmd[0] == 'cpy':
        src = cmd[1]
        dst = cmd[2]
        if is_number(src):
            reg[dst] = int(src)
        else:
            reg[dst] = reg[src]
        i += 1

    elif cmd[0] == 'jnz':
        src = cmd[1]
        jmp = int(cmd[2])
        if (is_number(src) and int(src) != 0) or reg[src] != 0:
            i += jmp
        else:
            i += 1

    elif cmd[0] == 'inc':
        src = cmd[1]
        reg[src] += 1
        i += 1

    elif cmd[0] == 'dec':
        src = cmd[1]
        reg[src] -= 1
        i += 1
    else:
        print(f"Bad line: {l}")

print(reg)
    # print(i)
