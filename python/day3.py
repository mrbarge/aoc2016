def valid(x, y, z):
    if x + y > z and x + z > y and y + z > x:
        print(f"Comparing {x}, {y} and {z} - valid")
        return True
    else:
        print(f"Comparing {x}, {y} and {z} - invalid")
        return False


with open('data/day3.input') as f:
    data = [e.strip().split() for e in f.readlines()]

valid_triangles = 0
for t in data:
    if valid(int(t[0]),int(t[1]),int(t[2])):
        valid_triangles += 1

print(f"Part 1: {valid_triangles}")

valid_triangles = idx = tries = 0
while idx+2 <= len(data):
    if valid(int(data[idx][0]), int(data[idx+1][0]), int(data[idx+2][0])):
        valid_triangles += 1
    if valid(int(data[idx][1]), int(data[idx + 1][1]), int(data[idx + 2][1])):
        valid_triangles += 1
    if valid(int(data[idx][2]), int(data[idx + 1][2]), int(data[idx + 2][2])):
        valid_triangles += 1
    idx += 3
    tries += 1

print(f"Part 2: {valid_triangles}")


