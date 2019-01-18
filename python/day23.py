from collections import defaultdict

with open('data/day23.input') as f:
    data = [e.strip() for e in f.readlines()]

def toggle(line):

    cmd = line.split()

    if len(cmd) == 2:
        # one argument instructions
        if cmd[0] == 'inc':
            return f"dec {cmd[1]}"
        else:
            return f"inc {cmd[1]}"

    elif len(cmd) > 2:
        # multi-arg instructions
        if cmd[0] == 'jnz':
            return f"cpy {' '.join(cmd[1:])}"
        else:
            return f"jnz {' '.join(cmd[1:])}"

    else:
        print(f"Hope this shouldn't happen")

def is_number(s):
    try:
        i = int(s)
        return True
    except (ValueError, TypeError):
        return False

reg = defaultdict(int)

i = 0

reg['a'] = 7

while i < len(data):

    print(f"{reg} - {data[i]}")

    cmd = data[i].split()

    if cmd[0] == 'cpy':
        src = cmd[1]
        dst = cmd[2]

        # validate cpy args
        if not is_number(dst):

            if is_number(src):
                reg[dst] = int(src)
            else:
                reg[dst] = reg[src]

        i += 1

    elif cmd[0] == 'jnz':
        src = cmd[1]
        dst = cmd[2]

        # validate jnz args
        if is_number(dst):
            jmp = int(dst)
        else:
            jmp = reg[dst]

        if is_number(src):
            cmp = int(src)
        else:
            cmp = reg[src]

        if 0 <= (i+jmp) < len(data):
            if cmp != 0:
                i += jmp
            else:
                i += 1
        else:
            i += 1
            continue

    elif cmd[0] == 'inc':
        src = cmd[1]
        reg[src] += 1
        i += 1

    elif cmd[0] == 'dec':
        src = cmd[1]
        reg[src] -= 1
        i += 1

    elif cmd[0] == 'tgl':

        if len(cmd) == 2 and is_number(cmd[1]) and (int(cmd[1]) + i) < len(data):
            new_cmd = toggle(data[int(cmd[1])+i])
            data[int(cmd[1])+i] = new_cmd
        elif len(cmd) == 2 and not is_number(cmd[1]):
            if 0 <= (reg[cmd[1]] + i) < len(data):
                new_cmd = toggle(data[reg[cmd[1]]+i])
                data[reg[cmd[1]] + i] = new_cmd

        i += 1
    else:
        print(f"Bad line: {cmd}")

print(reg)
