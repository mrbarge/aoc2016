from enum import Enum
from collections import defaultdict

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

    def send_low(self, chip, bintype):
        return (self.low_dest, self.chips[0])

    def send_high(self, chip, bintype):
        return (self.high_dest, self.chips[1])

    def add_chip(self, chip):
        self.chips.append(chip)
        self.chips.sort()

    def ready(self):
        return len(self.chips) >= 2

bots = defaultdict(Bot)

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

bots = {}
output = {}
input = {}


