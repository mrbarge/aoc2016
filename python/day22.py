import re
import sys

class Disk:

    def __init__(self, id, size, used):
        self.id = id
        self.size = size
        self.used = used

    def avail(self):
        return self.size - self.used

    def use(self):
        return int((self.used/self.size)*100)

def print_disks(disks):
    for y in range(0,len(disks)):
        for x in range(0,len(disks[0])):
            d = disks[y][x]
            sys.stdout.write(f"{d.used:3}T/{d.size:3}T  --  ")
        sys.stdout.write('\n')
        for x in range(0,len(disks[0])):
            sys.stdout.write(f"    |          ")
        sys.stdout.write('\n')



with open('data/day22.input') as f:
    data = [e.strip() for e in f.readlines()]

disks = []
pos_disks = [[None for x in range(0,38)] for y in range (0,28)]

for line in data:
    if line.startswith('/dev'):
        diskid = line.split()[0]
        m = re.match(r'.*x(\d+)-y(\d+)',diskid)
        if m:
            x = int(m[1])
            y = int(m[2])
        size = int(re.findall(r'\d+', line.split()[1])[0])
        used = int(re.findall(r'\d+', line.split()[2])[0])

        disk = Disk(line.split()[0],size,used)
        disks.append(disk)
        pos_disks[y][x] = disk

viable = 0
pairs = []
for diska in disks:
    for diskb in disks:
        pair2 = f"{diskb.id}-{diska.id}"
        if diska.id == diskb.id or diska.used == 0:
            continue

        if diska.used <= diskb.avail() and pair2 not in pairs:
            viable += 1
            pairs.append(pair2)

print(f"Part one: {viable}")

print_disks(pos_disks)