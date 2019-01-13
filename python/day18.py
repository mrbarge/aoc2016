with open('data/day18.input') as f:
    data = f.readline().strip()


def is_trap(s,n):
    if n < 0 or n >= len(s):
        return False
    else:
        return s[n] == '^'


def is_safe(s,n):
    if n < 0 or n >= len(s):
        return True
    else:
        return s[n] == '.'


def make_line(prev):
    ret = ''
    for i in range(0,len(prev)):
        if is_trap(prev,i-1) and is_trap(prev,i) and is_safe(prev,i+1):
            ret += '^'
        elif is_safe(prev,i-1) and is_trap(prev,i) and is_trap(prev,i+1):
            ret += '^'
        elif is_safe(prev,i-1) and is_safe(prev,i) and is_trap(prev,i+1):
            ret += '^'
        elif is_trap(prev,i-1) and is_safe(prev,i) and is_safe(prev,i+1):
            ret += '^'
        else:
            ret += '.'
    return ret


def count_safe(lines):
    return sum(l.count('.') for l in lines)

lines = [data]
for i in range(1,40):
    lines.append(make_line(lines[i-1]))

print(f"Part one: {count_safe(lines)}")

lines = [data]
for i in range(1,400000):
    lines.append(make_line(lines[i-1]))

print(f"Part two: {count_safe(lines)}")

