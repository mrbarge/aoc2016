import re

def swap_pos(word,x,y):
    ret = [c for c in word]
    t = ret[x]
    ret[x] = ret[y]
    ret[y] = t
    return ''.join(ret)

def swap_letter(word,x,y):
    ret = ''
    for i in range(0,len(word)):
        if word[i] == x:
            ret += y
        elif word[i] == y:
            ret += x
        else:
            ret += word[i]
    return ret

def reverse(word,x,y):
    return word[:x] + ''.join(reversed(word[x:y+1])) + word[y+1:]

def rotate_left(word,x):
    return rotate_right(word,len(word)-x)

def rotate_right(word,x):
    ret = [c for c in word]
    x = x % len(word)
    for i in range(0,len(word)):
        ret[x] = word[i]
        x = (x + 1) % len(word)
    return ''.join(ret)

def move(word,x,y):
    ret = [x for x in word]
    chr = ret.pop(x)
    ret.insert(y,chr)
    return ''.join(ret)

def rotate_pos(word,x):
    xidx = word.find(x)
    if xidx >= 4:
        return rotate_right(word,2 + xidx)
    else:
        return rotate_right(word,1 + xidx)

def rotate_inverse_pos(word,x):
    xidx = word.find(x)
    if xidx <= 1:
        return rotate_left(word,1)
    elif xidx == 2:
        return rotate_right(word,2)
    elif xidx == 3:
        return rotate_left(word,2)
    elif xidx == 4:
        return rotate_right(word,1)
    elif xidx == 5:
        return rotate_left(word,3)
    elif xidx == 6:
        return word
    elif xidx == 7:
        return rotate_right(word,4)

input = 'abcdefgh'

with open('data/day21.input') as f:
    data = [e.strip() for e in f.readlines()]

for line in data:
    if line.startswith('swap position'):
        x = int(line.split()[2])
        y = int(line.split()[5])
        input = swap_pos(input,x,y)
    elif line.startswith('swap letter'):
        x = line.split()[2]
        y = line.split()[5]
        input = swap_letter(input,x,y)
    elif line.startswith('reverse positions'):
        x = int(line.split()[2])
        y = int(line.split()[4])
        input = reverse(input,x,y)
    elif line.startswith('rotate left'):
        x = int(line.split()[2])
        input = rotate_left(input,x)
    elif line.startswith('rotate right'):
        x = int(line.split()[2])
        input = rotate_right(input,x)
    elif line.startswith('move'):
        x = int(line.split()[2])
        y = int(line.split()[5])
        input = move(input,x,y)
    elif line.startswith('rotate based'):
        x = line.split()[6]
        input = rotate_pos(input,x)
    else:
        print(f"No idea: {line}")

print(f"Part one: {input}")

input = 'fbgdceah'
for line in reversed(data):
    if line.startswith('swap position'):
        x = int(line.split()[2])
        y = int(line.split()[5])
        input = swap_pos(input,y,x)
    elif line.startswith('swap letter'):
        x = line.split()[2]
        y = line.split()[5]
        input = swap_letter(input,y,x)
    elif line.startswith('reverse positions'):
        x = int(line.split()[2])
        y = int(line.split()[4])
        input = reverse(input,x,y)
    elif line.startswith('rotate left'):
        x = int(line.split()[2])
        input = rotate_right(input,x)
    elif line.startswith('rotate right'):
        x = int(line.split()[2])
        input = rotate_left(input,x)
    elif line.startswith('move'):
        x = int(line.split()[2])
        y = int(line.split()[5])
        input = move(input,y,x)
    elif line.startswith('rotate based'):
        x = line.split()[6]
        input = rotate_inverse_pos(input,x)
    else:
        print(f"No idea: {line}")

print(f"Part two: {input}")