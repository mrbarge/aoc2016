from enum import Enum
from collections import defaultdict

def find_next_bot(bots):
    for botid in bots:
        if len(bots[botid].chips) >= 2:
            return botid
    return -1



with open('data/day10.input') as f:
    data = [e.strip() for e in f.readlines()]

class Dest(Enum):
    BOT = 1
    OUTPUT = 2

class Bot:

    def __init__(self):
        self.chips = []
        self.low_dest = None
        self.high_dest = None
        self.low_type = None
        self.high_type = None

    def send_low(self):
        return (self.low_dest, self.chips[0])

    def send_high(self):
        return (self.high_dest, self.chips[1])

    def add_chip(self, chip):
        self.chips.append(chip)
        self.chips.sort()

    def ready(self):
        return len(self.chips) >= 2

bots = defaultdict(Bot)
outputs = defaultdict(list)

for line in data:
    if line.startswith('value'):
        chip_id = int(line.split()[1])
        bot_id = int(line.split()[5])

        bots[bot_id].add_chip(chip_id)

    else:
        source_bot_id = int(line.split()[1])
        low_type = line.split()[5]
        low_id = int(line.split()[6])
        high_type = line.split()[10]
        high_id = int(line.split()[11])

        bots[source_bot_id].low_type = low_type
        bots[source_bot_id].high_type = high_type
        bots[source_bot_id].low_dest = low_id
        bots[source_bot_id].high_dest = high_id


done = False
outputbin = {}

while not done:

    botid = find_next_bot(bots)

    if botid < 0:
        done = True
        continue

    if bots[botid].send_low()[1] == 17 and bots[botid].send_high()[1] == 61:
        print(f"Part one: {botid}")

    if bots[botid].low_type == 'output':
        outputs[bots[botid].low_dest] = bots[botid].send_low()[1]
    else:
        bots[bots[botid].low_dest].add_chip(bots[botid].send_low()[1])

    if bots[botid].high_type == 'output':
        outputs[bots[botid].high_dest] = bots[botid].send_high()[1]
    else:
        bots[bots[botid].high_dest].add_chip(bots[botid].send_high()[1])

    bots[botid].chips = []

print(f"Part two: {outputs[0] * outputs[1] * outputs[2]}")
