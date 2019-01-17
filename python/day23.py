from collections import defaultdict

with open('data/day23.input') as f:
    data = [e.strip() for e in f.readlines()]

def toggle(cmd):

    if len(cmd) == 2:
        # one argument instructions
        if cmd[0] == 'inc':
            return f"dec {cmd[1]}"
        else:
            return ' '.join(cmd)

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

        # validate jnz args
        if is_number(dst):
            jmp = int(cmd[2])
            if (is_number(src) and int(src) != 0) or reg[src] != 0:
                i += jmp
            else:
                i += 1
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

    elif cmd[0] == 'tgl':

        if len(cmd) == 2 and is_number(cmd[1]) and (int(cmd[1]) + i) < len(data):
            new_cmd = toggle(cmd)
            data[int(cmd[1])+i] = new_cmd
        elif len(cmd) == 2 and not is_number(cmd[1]):
            if (reg[cmd[1]] + i) < len(data):
                new_cmd = toggle(cmd)
                data[reg[cmd[1]] + i] = new_cmd

        i += 1
    else:
        print(f"Bad line: {cmd}")

print(reg)
    # print(i)
