from collections import defaultdict
import sys

def is_wall(x, y, n):
    v = x*x + 3*x + 2*x*y + y + y*y + n
    o = format(v, "b").count("1")
    if o % 2 == 0:
        return False
    else:
        return True

def get_neighbours(x,y):
    return [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]

def print_grid(grid):
    for y in range(0,100):
        for x in range(0,100):
            if grid[(x,y)]:
                sys.stdout.write('#')
            else:
                sys.stdout.write('.')
        sys.stdout.write('\n')

def search(grid, source, dest):
    assert source in grid, 'Starting node does not exist'
    assert dest in grid, 'Destination node does not exist'

    inf = float('inf')

    # record min distance to coord
    distances = {coord: inf for coord in grid.keys()}
    distances[source] = 0

    # record best parent step to coord
    parent_node = {coord: None for coord in grid.keys()}

    # unvisited nodes
    unvisited = grid.keys()

    while unvisited:
        # find next, shortest node to visit
        next_node = min(unvisited, key=lambda c: distances[c])

        neighbours = get_neighbours(next_node[0], next_node[1])
        for n in neighbours:
            # verify neighbour is a valid coord
            if n not in grid:
                continue

            next_dist = distances[next_node] + 1

            if next_dist < distances[n]:
                distances[n] = next_dist
                parent_node[n] = next_node

        grid.pop(next_node)

    path = []
    iternode = dest
    while parent_node[iternode] is not None:
        path.append(iternode)
        iternode = parent_node[iternode]

    print(path)
    return len(path)

n = 1364
# n = 10
grid = defaultdict(bool)

for x in range(0,100):
    for y in range(0,100):
        if not is_wall(x,y,n):
            grid[(x,y)] = True

start = (1,1)
dest = (31,39)
# dest = (7,4)
steps = search(grid,start,dest)
print(f"Part one: {steps}")