class Elf:
    def __init__(self, id):
        self.id = id
        self.has_present = True

def check(elves):
    return len([x for x in elves if x.has_present])

def freed(elves):
    return [x.id for x in elves if x.has_present]

def clean(elves):
    for x in elves:
        if not x.has_present:
            elves.remove(x)

def find_next_present(elves,n):
    done = False
    l = len(elves)
    i = (n+1) % l
    while i != n:
        if elves[i].has_present:
            return i
        i = (i+1) % l

    return -1

def step(elves):
    for i in range(0,len(elves)):
        if not elves[i].has_present:
            continue
        ni = find_next_present(elves,i)
        # ni = (i+1) % len(elves)
        if ni >= 0:
            elves[i].has_present = True
            elves[ni].has_present = False
            i = ni
        else:
            return elves
    return elves


elves = [Elf(x) for x in range(0,3012210)]

while True:
    elves = step(elves)
    # clean(elves)
    fre = freed(elves)
    if len(fre) == 1:
        print(f"Part one: {fre[0]+1}")
        break

n = 1
while (n*3) < 3012210:
    n *= 3
print(f"Part two: {3012210-n}")