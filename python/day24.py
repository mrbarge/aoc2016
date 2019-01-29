import networkx as nx
from collections import defaultdict
from itertools import permutations

with open('data/day24.input') as f:
    data = [e.strip() for e in f.readlines()]

graph = nx.generators.lattice.grid_2d_graph(len(data),len(data[0]))
nodes = defaultdict(tuple)

for y in range(0,len(data)):
    for x in range(0,len(data[0])):
        if data[y][x] == '#':
            # remove any useless nodes (Walls)
            graph.remove_node((y,x))
        elif data[y][x].isdigit():
            nodes[int(data[y][x])] = (y,x)

# for each unique node pair, find the shortest path between them
shortest_paths = defaultdict(list)
for i in nodes.keys():
    for j in nodes.keys():
        if i == j:
            continue
        path = nx.shortest_path_length(graph,nodes[i],nodes[j])
        shortest_paths[(i,j)] = path
        shortest_paths[(j,i)] = path

def process(part2=False):
    # for each possible walking path..
    min_walk_len = float('inf')
    min_walk = None
    for walk in permutations(range(1,8)):
        # add the start node
        walk = [0] + list(walk)
        if part2:
            walk += [0]

        total_len = 0
        for i in range(0,(len(walk)-1)):
            total_len += shortest_paths[(walk[i],walk[i+1])]

        if float(total_len) < min_walk_len:
            min_walk_len = float(total_len)
            min_walk = walk

    print(f"Min walk length: {min_walk_len}")
    print(f"Min walk: {walk}")

process()
process(part2=True)
