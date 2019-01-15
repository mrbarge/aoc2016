with open('data/day20.input') as f:
    data = [e.strip() for e in f.readlines()]

class Ip:
    def __init__(self, num, begin):
        self.num = num
        self.begin = begin

    def __str__(self):
        if self.begin:
            return f"b{self.num}"
        else:
            return f"e{self.num}"

ips = []

for line in data:
    lower = float(line.split('-')[0])
    upper = float(line.split('-')[1])

    ips.append(Ip(lower,True))
    ips.append(Ip(upper,False))

ips.sort(key=lambda x: x.num)

allips = 0
lowest = ips[0].num
part1 = -1
i = 0
while i < len(ips):
    if ips[i].begin and (ips[i].num > (lowest+1)):
        # we have found a gap between our lowest and our next 'begin-start'
        # so this marks the first 'free' block.. i think
        if part1 < 0:
            part1 = lowest+1
        # for part 2, increment the running tally with the range between
        # the last seen end and the next begin
        allips += (ips[i].num - lowest - 1)

    if ips[i].begin:
        # find last end
        i += 1
        bcount = 1
        while i < len(ips):
            if ips[i].begin:
                bcount += 1
            else:
                bcount -= 1
                if bcount == 0:
                    # shift our 'lowest' to the end block
                    lowest = ips[i].num
                    i += 1
                    break
            i += 1
    else:
        break

print(f"part one: {part1}")
print(f"part two: {allips}")