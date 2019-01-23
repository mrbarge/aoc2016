import hashlib
import re

input = 'jlmsuwbz'

hashes = []
stretched_hashes = []

def has_triplet(s):
    matches = re.findall(r'((\w)\2{2,})', s)
    return [m[1] for m in matches]

def has_quintet(s,c):
    srch = ''.join(str(c)*5)
    p = re.compile(srch)
    return re.findall(p,s)

def stretch_hash(s):
    hashstr = s
    for i in range(0,2016):
        m = hashlib.new('md5')
        m.update(str.encode(hashstr))
        hashstr = m.hexdigest()
    return hashstr

def solve(h, n):
    keys = 0
    for i in range(0, 50000):
        chr = has_triplet(h[i])
        if chr:
            c = chr[0]
            for j in range(i + 1, i + 1001):
                if j < len(h) and has_quintet(h[j], c):
                    keys += 1
                    break
        if keys == n:
            return i
    return -1

for i in range(0,50000):
    m = hashlib.new('md5')
    key = f"{input}{i}"
    m.update(str.encode(key))

    md5hash = m.hexdigest()
    hashes.append(md5hash)

for i in range(0,50000):
    m = hashlib.new('md5')
    key = f"{input}{i}"
    m.update(str.encode(key))
    md5hash = m.hexdigest()
    stretched_hashes.append(stretch_hash(md5hash))


print(f"Part one: {solve(hashes,64)}")
print(f"Part two: {solve(stretched_hashes,64)}")
