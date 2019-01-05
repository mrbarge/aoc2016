from collections import defaultdict
from collections import Counter
import itertools


with open('data/day4.input') as f:
    data = [e.strip() for e in f.readlines()]

sector_sum = 0
for line in data:
    checksum = line[line.find('[')+1:line.find('[')+6]
    encrypted_name = line[:line.rfind('-')].replace('-','')
    sector_id = line[line.rfind('-')+1:line.rfind('[')]

    charcount = Counter(encrypted_name).most_common()

    # convert count to negative so it can be sorted ascending alongside lettering
    neg_charcount = [(l, -v) for l, v in charcount]
    sorted_negcharcount = sorted(neg_charcount, key=lambda t: (t[1],t[0]))

    real_room = True
    for letter, count in sorted_negcharcount[0:5]:
        if letter not in checksum:
            real_room = False

    if real_room:
        sector_sum += int(sector_id)

print(f"Part one: {sector_sum}")