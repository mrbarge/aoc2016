import hashlib

def is_door(c):
    if c in ['b','c','d','e','f']:
        return True
    else:
        return False

def move(pos, dir):
    if dir == 'U':
        return pos[0], pos[1]-1
    elif dir == 'D':
        return pos[0], pos[1]+1
    elif dir == 'L':
        return pos[0]-1, pos[1]
    else:
        return pos[0]+1, pos[1]

def can_move(pos, dir):
    return (dir == 'U' and pos[1] > 0) or (dir == 'D' and pos[1] < 3) or (dir == 'L' and pos[0] > 0) or (dir == 'R' and pos[0] < 3)

def set_doors(code, walk):
    s = code + ''.join(walk)
    m = hashlib.new('md5')
    key = f"{s}"
    m.update(str.encode(key))
    md5hash = m.hexdigest()

    doors = {
        'U': is_door(md5hash[0]),
        'D': is_door(md5hash[1]),
        'L': is_door(md5hash[2]),
        'R': is_door(md5hash[3]),
    }
    return doors

input = 'udskfozm'
failed_walks = []
good_walks = []
done = False

def bfs_search(start, goal):
    queue = [(start, [])]
    while queue:
        # print(f"Queue looks like: {queue}")
        pos, path = queue.pop(0)
        next_doors = set_doors(input, path)
        for dir in [x for x in next_doors.keys() if next_doors[x]]:
            if list(next_doors.values()).count(True) == 0:
                # dead end
                # print(f"Found dead end: {path}")
                pass
            elif move(pos,dir) == goal:
                # got to goal
                yield path + [dir]
            elif can_move(pos, dir):
                # move to next
                queue.append((move(pos, dir), path + [dir]))
            else:
                pass
                # print(f"Found dead end: {path}")

paths = list(bfs_search((0,0),(3,3)))
paths.sort(key = lambda s: len(s))
print(f"Part one: {''.join(paths[0])}")
print(f"Part two: {len(paths[len(paths)-1])}")

