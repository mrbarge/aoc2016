import re

with open('data/day9.input') as f:
    data = f.readline().strip()

marker_pattern = re.compile('.*?(\d+)x(\d+).*?')

booty = ''

i = 0
while i < len(data):

    if data[i] == '(':
        # in marker

        # find closing bracket
        ei = data.find(')',i)

        # extract marker info
        m = re.match(marker_pattern, data[i:ei])
        if m:
            numchar = int(m.group(1))
            repeat = int(m.group(2))
        else:
            print(f"borked: {data[i:ei]}")

        # move to the end of the marker
        i = ei + 1

        # and build up our decompressed string
        bits = data[i:i+numchar]

        for j in range(0,repeat):
            booty += bits

        # move to the end of the marker block
        i += numchar
    else:
        # just chuck it on the end
        booty += data[i]
        i += 1

print(len(booty))

