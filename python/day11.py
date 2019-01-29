from enum import Enum
from collections import defaultdict

class Generator(Enum):
    PROMETHIUM = -1
    COBALT = -2
    PLUTONIUM = -3
    CURIUM = -4
    RUTHIEM = -5
    ELERIUM = -6
    DILITHIUM = -7


class Chip(Enum):
    PROMETHIUM = 1
    COBALT = 2
    PLUTONIUM = 3
    CURIUM = 4
    RUTHIEM = 5
    ELERIUM = 6
    DILITHIUM = 7

def is_complete(floor):
    return len(floor)+1 == 10
    # s = sum([x.value for x in floor])
    # return s == 0

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


def load_from_floor(elevator, floors, floor_num):
    while not elevator_full(elevator) and len(floors[floor_num]) > 0:
        elevator.append(floors[floor_num].pop())
    return elevator, floors


def elevator_full(elevator):
    return len(elevator) == 2


def load_from_elevator(elevator, floors, floor_num):
    if len(elevator) > 0:
        floors[floor_num].append(elevator.pop())
    return elevator, floors


floors = defaultdict(list)

floors[1] = [Generator.PROMETHIUM,Chip.PROMETHIUM,Generator.DILITHIUM,Chip.DILITHIUM,Generator.ELERIUM,Chip.ELERIUM]
floors[2] = [Generator.COBALT,Generator.CURIUM,Generator.RUTHIEM,Generator.PLUTONIUM]
floors[3] = [Chip.COBALT,Chip.CURIUM,Chip.RUTHIEM,Chip.PLUTONIUM]
floors[4] = []

seen = []
elevator = []
elevator_floor = 1
moves = 0

# Load the elevator with the first two elements in the first floor
elevator, floors = load_from_floor(elevator, floors, elevator_floor)

while not is_complete(floors[4]):

    while not elevator_full(elevator) and elevator_floor > 1:
        elevator_floor -= 1
        elevator, floors = load_from_floor(elevator, floors, elevator_floor)
        moves += 1

    while elevator_floor < 4:
        elevator_floor += 1
        elevator, floors = load_from_floor(elevator, floors, elevator_floor)
        moves += 1

    # unload on top floor
    load_from_elevator(elevator, floors, 4)

    print(f"elevator: {elevator} floors: {floors[4]}")

print(f"Part two: {moves}")

