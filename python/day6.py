from collections import defaultdict
import operator

with open('data/day6.input') as f:
    data = [e.strip() for e in f.readlines()]

seen = defaultdict(lambda: defaultdict(int))
for line in data:
    i = 0
    while i < len(line):
        seen[i][line[i]] += 1
        i += 1

# part one
print("Part one..")
for k in seen:
    sorted_entries = sorted(seen[k].items(), key=operator.itemgetter(1), reverse=True)
    print(sorted_entries[0])

# part wo
print("Part two..")
for k in seen:
    sorted_entries = sorted(seen[k].items(), key=operator.itemgetter(1))
    print(sorted_entries[0])
