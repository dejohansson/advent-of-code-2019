import math

def load_lines(file_name):
    with open(file_name, "r") as f:
        return f.read().split("\n")

mapp = load_lines("day10/map.txt")
load_lines("day10/test1")
load_lines("day10/test2")
load_lines("day10/test3")
load_lines("day10/test4")

def between(a, b, c):
    crossproduct = (c[1] - a[1]) * (b[0] - a[0]) - (c[0] - a[0]) * (b[1] - a[1])
    if abs(crossproduct) != 0:
        return False

    dotproduct = (c[0] - a[0]) * (b[0] - a[0]) + (c[1] - a[1])*(b[1] - a[1])
    if dotproduct < 0:
        return False

    squaredlengthba = (b[0] - a[0])*(b[0] - a[0]) + (b[1] - a[1])*(b[1] - a[1])
    if dotproduct > squaredlengthba:
        return False

    return True

asteroids = []
for y, line in enumerate(mapp):
    for x, val in enumerate(line):
        if val == "#":
            asteroids.append((x,y))

seen = {}
best = ((0,0), 0)
for a in asteroids:
    s = []
    for b in asteroids:
        if b != a:
            obstructed = False
            if not((a in seen and b in seen[a]) or (b in seen and a in seen[b])):
                for c in asteroids:
                    if c != a and c != b and between(a, b, c):
                        obstructed = True
                        break
            if not obstructed:
                s.append(b)
    seen[a] = s
    if len(s) > best[1]:
        best = (a, len(s))
print(best)

angles = []
x_b = best[0][0]
y_b = best[0][1]
for (x, y) in seen[best[0]]:
    a = math.atan2(-1*(y-y_b), x-x_b)
    if a > math.pi/2:
        a -= 2*math.pi
    angles.append(((x, y), a))
angles.sort(key=lambda c: c[1])
angles.reverse()
print(angles[199][0][0]*100+angles[199][0][1])