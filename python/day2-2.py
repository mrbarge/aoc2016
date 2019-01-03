valid_buttons = [
    (3,1),
    (2,2), (3,2), (4,2),
    (1,3), (2,3), (3,3), (4,3), (5,3),
    (2,4), (3,4), (4,4),
    (3,5)
]

def move(from_coord, to_coord):
    if to_coord in valid_buttons:
        return to_coord
    else:
        return from_coord

def posToButton(coord):
    return {
        (3,1): "1",
        (2,2): "2", (3,2): "3", (4,2): "4",
        (1,3): "5", (2,3): "6", (3,3): "7", (4,3): "8", (5,3): "9",
        (2,4): "A", (3,4): "B", (4,4): "C",
        (3,5): "D"
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

coord = (1,3)
for line in data:
    digit, coord = walk(line, coord)
    print(digit)