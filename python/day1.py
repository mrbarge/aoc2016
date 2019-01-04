from enum import Enum


class Dir(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4


def newdir(currdir, turn):
    if currdir == Dir.NORTH:
        return {
            'L': Dir.WEST,
            'R': Dir.EAST
        }[turn]
    elif currdir == Dir.SOUTH:
        return {
            'L': Dir.EAST,
            'R': Dir.WEST
        }[turn]
    elif currdir == Dir.EAST:
        return {
            'L': Dir.NORTH,
            'R': Dir.SOUTH
        }[turn]
    elif currdir == Dir.WEST:
        return {
            'L': Dir.SOUTH,
            'R': Dir.NORTH
        }[turn]


def walk(x, y, direction):
    if direction == Dir.NORTH:
        return x, y + 1
    elif direction == Dir.SOUTH:
        return x, y - 1
    elif direction == Dir.EAST:
        return x + 1, y
    elif direction == Dir.WEST:
        return x - 1, y


with open('data/day1.input') as f:
    data = [e.strip() for e in f.readline().split(',')]

coord = hqcoord = (0,0)
currdir = Dir.NORTH
foundFirstDupe = False
seen = {}

for step in data:
    currdir = newdir(currdir, step[0])
    for i in range(0,int(step[1:])):
        coord = walk(coord[0], coord[1], currdir)
        if coord in seen and not foundFirstDupe:
            hqcoord = coord
            foundFirstDupe = True
        else:
            seen[coord] = True

blocks = abs(coord[0]) + abs(coord[1])
print(f"Part 1: {blocks}")
p2blocks = abs(hqcoord[0]) + abs(hqcoord[1])
print(f"Part 2: {p2blocks}")
