from enum import Enum
from collections import defaultdict

class Generator(Enum):
    PROMETHIUM = -1
    COBALT = -2
    PLUTONIUM = -3
    CURIUM = -4
    RUTHIEM = -5


class Chip(Enum):
    PROMETHIUM = 1
    COBALT = 2
    PLUTONIUM = 3
    CURIUM = 4
    RUTHIEM = 5

def is_complete(floor):
    s = sum([x.value for x in floor])
    return s == 0

def valid_floor(floor):
    for c in Chip:
        cgen = Generator(-(c.value))
        if c in floor and cgen not in floor:
            if sum([True for g in Generator if g in floor and abs(g.value) != c.value]) > 0:
                return False
    return True

def floors_to_list(floors):
    ret = []
    for f in range(0,len(floors)):
        for x in sorted([x.value for x in floors[f]]):
            ret.append((f,x))
    return ret

floors = defaultdict(list)

floors[1] = [Generator.PROMETHIUM,Chip.PROMETHIUM]
floors[2] = [Generator.COBALT,Generator.CURIUM,Generator.RUTHIEM,Generator.PLUTONIUM]
floors[3] = [Chip.COBALT,Chip.CURIUM,Chip.RUTHIEM,Chip.PLUTONIUM]
floors[4] = []

seen = []
elevator = 1

# while not is_complete(floors[1]):

