import hashlib

secret_key = 'cxdnnyjw'

p1password = ''
key_num = 0
while len(p1password) < 8:
    m = hashlib.new('md5')
    key = f"{secret_key}{key_num}"
    m.update(str.encode(key))

    md5hash = m.hexdigest()
    if md5hash.startswith('00000'):
        p1password += md5hash[5]

    key_num += 1

print(f"Part one: {p1password}")

p2password = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
key_num = 0
while sum(v == ' ' for v in p2password) > 0:
    m = hashlib.new('md5')
    key = f"{secret_key}{key_num}"
    m.update(str.encode(key))

    md5hash = m.hexdigest()
    if md5hash.startswith('00000') and str.isdigit(md5hash[5]) and 0 <= int(md5hash[5]) < 8 and p2password[int(md5hash[5])] == ' ':
        p2password[int(md5hash[5])] = md5hash[6]
        print(p2password)

    key_num += 1


print(f"Part two: {''.join(p2password)}")