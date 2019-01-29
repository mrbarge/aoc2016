from collections import defaultdict
import sys

def is_finished(maze):
    if maze[0][0] == True and maze[1][2] == True and maze[2][17] == True and maze[3][10] == True and maze[4][3] == True and maze[5][0] == True:
        return True
    else:
        return False

def is_p2_finished(maze):
    if maze[0][0] == True and maze[1][2] == True and maze[2][17] == True and maze[3][10] == True and maze[4][3] == True and maze[5][0] == True and maze[6][5] == True:
        return True
    else:
        return False

def tick(maze):
    for disc in maze:
        # find slot in row
        i = [i for i,v in enumerate(maze[disc]) if v == True]
        npos = (i[0] + 1) % len(maze[disc])
        # rotate the row
        maze[disc][i[0]] = False
        maze[disc][npos] = True
    return maze

def print_maze(maze):
    for disc in maze:
        for i in range(0,len(maze[disc])):
            if maze[disc][i] == False:
                sys.stdout.write('X')
            else:
                sys.stdout.write('O')
        sys.stdout.write('\n')
    sys.stdout.write('\n')

maze = defaultdict(list)
maze[0] = [False for x in range(0,17)]
maze[1] = [False for x in range(0,3)]
maze[2] = [False for x in range(0,19)]
maze[3] = [False for x in range(0,13)]
maze[4] = [False for x in range(0,7)]
maze[5] = [False for x in range(0,5)]
maze[0][15] = maze[1][2] = maze[2][4] = maze[3][2] = maze[4][2] = maze[5][0] = True

# maze = defaultdict(list)
# maze[0] = [False for x in range(0,5)]
# maze[1] = [False for x in range(0,2)]
# maze[0][4] = maze[1][1] = True
# print_maze(maze)

i = 0
while True:
    if not is_finished(maze):
        maze = tick(maze)
        i += 1
    else:
        break

# deduct one to be the time before it enters slot 0
print(f"Part one: {i-1}")

# reset state for part 2
maze = defaultdict(list)
maze[0] = [False for x in range(0,17)]
maze[1] = [False for x in range(0,3)]
maze[2] = [False for x in range(0,19)]
maze[3] = [False for x in range(0,13)]
maze[4] = [False for x in range(0,7)]
maze[5] = [False for x in range(0,5)]
maze[6] = [False for x in range(0,11)]
maze[0][15] = maze[1][2] = maze[2][4] = maze[3][2] = maze[4][2] = maze[5][0] = maze[6][0] = True

i = 0
while True:
    if not is_p2_finished(maze):
        maze = tick(maze)
        i += 1
    else:
        break
print(f"Part two: {i-1}")
