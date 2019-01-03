valid_buttons = [
    (1,1), (2,1), (3,1),
    (1,2), (2,2), (3,2),
    (1,3), (2,3), (3,3)
]

def move(from_coord, to_coord):
    if to_coord in valid_buttons:
        return to_coord
    else:
        return from_coord

def posToButton(coord):
    return {
        (1,1): 1, (2,1): 2, (3,1): 3,
        (1,2): 4, (2,2): 5, (3,2): 6,
        (1,3): 7, (2,3): 8, (3,3): 9
    }[coord]

def walk(line, coord):
    for c in line:
        if c == 'R':
            coord = move(coord, (coord[0]+1,coord[1]))
        elif c == 'L':
            coord = move(coord, (coord[0]-1,coord[1]))
        elif c == 'U':
            coord = move(coord, (coord[0],coord[1]-1))
        elif c == 'D':
            coord = move(coord, (coord[0],coord[1]+1))

    return posToButton(coord), coord

with open('day2.input') as f:
    data = f.readlines()

coord = (2,2)
for line in data:
    digit, coord = walk(line, coord)
    print(digit)