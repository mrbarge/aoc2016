input = '10011111011011001'

def step(a):
    b = ''.join(reversed(a)).replace('1','x').replace('0','1').replace('x','0')
    return ''.join([a,'0',b])

def checksum(s):
    first = True
    ret = s

    while first or (len(ret) % 2 == 0 and not first):
        first = False
        next = ''
        for i in range(0,len(ret),2):
            if ret[i] == ret[i+1]:
                next += '1'
            else:
                next += '0'
        ret = next

    return ret

disk_size = 35651584
data = input
while len(data) < disk_size:
    data = step(data)

print(checksum(data[0:disk_size]))