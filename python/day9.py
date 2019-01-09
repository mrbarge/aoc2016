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

print(f"Part one: {len(booty)}")

def decompress(s):

    retlen = 0
    i = 0
    while i < len(s):
        if s[i] == '(':
            # find closing bracket
            ei = s.find(')', i)

            # extract marker info
            m = re.match(marker_pattern, s[i:ei])
            if m:
                numchar = int(m.group(1))
                repeat = int(m.group(2))
            else:
                print(f"borked: {s[i:ei]}")

            # move to the end of the marker
            i = ei + 1

            # and build up our decompressed string
            bits = s[i:i + numchar]

            bl = decompress(bits)
            retlen += bl
            for j in range(1,repeat):
                retlen += bl

            # move to the end of the marker block
            i += numchar

        else:
            # just chuck it on the end
            retlen += 1
            i += 1

    return retlen

bootylen = 0
i = 0
l = decompress(data)
print(f"PArt two: {l}")
