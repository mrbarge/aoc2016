import re
import sys

def shift_row(screen, axis, axisval):
    data_to_shift = [screen[axis][i] for i in range(0,width)]

    for i in range(0,width):
        screen[axis][i] = False

    for i in range(0,width):
        pos_mod = (i + axisval) % width
        screen[axis][pos_mod] = data_to_shift[i]

    return screen


def shift_col(screen, axis, axisval):
    data_to_shift = [screen[i][axis] for i in range(0,height)]

    for i in range(0,height):
        screen[i][axis] = False

    for i in range(0,height):
        pos_mod = (i + axisval) % height
        screen[pos_mod][axis] = data_to_shift[i]

    return screen


def print_screen(screen):
    num = 0
    for i in range(0,len(screen)):
        for j in range(0,len(screen[i])):
            if screen[i][j] == True:
                sys.stdout.write('#')
            else:
                sys.stdout.write('.')
        sys.stdout.write('\n')

def count_lit(screen):
    num = 0
    for i in range(0,len(screen)):
        for j in range(0,len(screen[i])):
            if screen[i][j] == True:
                num += 1
    return num

rect_pattern = re.compile('rect (\d+)x(\d+)')
rotate_pattern = re.compile('rotate (.+) (.)=(\d+) by (\d+)')

with open('data/day8.input') as f:
    data = [e.strip() for e in f.readlines()]

width = 50
height = 6
# width = 7
# height = 3

screen = [[False for y in range(0,width)] for x in range(0,height)]

for line in data:
    if line.startswith('rect'):
        m = re.match(rect_pattern, line)
        x = int(m.group(1))
        y = int(m.group(2))

        for j in range(0, y):
            for i in range(0, x):
                screen[j][i] = True

    elif line.startswith('rotate row'):
        m = re.match(rotate_pattern, line)
        axisval = int(m.group(3))
        val = int(m.group(4))

        screen = shift_row(screen, axisval, val)

    elif line.startswith('rotate column'):
        m = re.match(rotate_pattern, line)
        axisval = int(m.group(3))
        val = int(m.group(4))

        screen = shift_col(screen, axisval, val)

    else:
        print(f"Bad input: {line}")

print(count_lit(screen))
print_screen(screen)

