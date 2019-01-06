from string import ascii_lowercase
from collections import Counter


def rot_n(n):
    az = ascii_lowercase
    letter_pos = {letter: str(index) for index, letter in enumerate(az, start=0)}
    rot_spaces = n % len(az)
    rot_az = ''
    for l in az:
        rot_az += az[(int(letter_pos[l]) + rot_spaces) % len(az)]

    return str.maketrans(az, rot_az)

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

for line in data:
    encrypted_name = line[:line.rfind('-')].replace('-', '')
    sector_id = line[line.rfind('-') + 1:line.rfind('[')]

    cipher = rot_n(int(sector_id))
    print(f"{encrypted_name.translate(cipher)} {sector_id}")

