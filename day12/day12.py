moons = [[[1, 4, 4], [0, 0, 0]],
        [[-4, -1, 19], [0, 0, 0]],
        [[-15, -14, 12], [0, 0, 0]],
        [[-17, 1, 10], [0, 0, 0]],]

"""moons = [[[-8, -10, 0], [0, 0, 0]],
        [[5, 5, 10], [0, 0, 0]],
        [[2, -7, 3], [0, 0, 0]],
        [[9, -8, -3], [0, 0, 0]],]"""

"""moons = [[[-1,0,2], [0, 0, 0]],
        [[2,-10,-7], [0, 0, 0]],
        [[4,-8,8], [0, 0, 0]],
        [[3,5,-1], [0, 0, 0]],]"""

for s in range(1000):
    for i, moon in enumerate(moons):
        for moon2 in moons[i:]:
            if moon[0][0] > moon2[0][0]:
                moon[1][0] -= 1
                moon2[1][0] += 1
            elif moon[0][0] < moon2[0][0]:
                moon[1][0] += 1
                moon2[1][0] -= 1

            if moon[0][1] > moon2[0][1]:
                moon[1][1] -= 1
                moon2[1][1] += 1
            elif moon[0][1] < moon2[0][1]:
                moon[1][1] += 1
                moon2[1][1] -= 1

            if moon[0][2] > moon2[0][2]:
                moon[1][2] -= 1
                moon2[1][2] += 1
            elif moon[0][2] < moon2[0][2]:
                moon[1][2] += 1
                moon2[1][2] -= 1
        
    for moon in moons:
        moon[0][0] += moon[1][0]
        moon[0][1] += moon[1][1]
        moon[0][2] += moon[1][2]

energy = 0
for moon in moons:
    pot = 0
    kin = 0
    for p in moon[0]:
        pot += abs(p)
    for v in moon[1]:
        kin += abs(v)
    print(pot, kin)
    energy += pot*kin
print(energy)

def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm

points = []
start = [tuple([(moon[0][i], moon[1][i]) for moon in moons]) for i in range(3)]
time = [0,0,0]

for t in range(3):
    num = 0
    while True:
        pt = tuple([(moon[0][t], moon[1][t]) for moon in moons])
        if num != 0 and pt == start[t]:
            time[t] = num
            break
            
        num += 1
        for i, moon in enumerate(moons):
            for moon2 in moons[i:]:
                if moon[0][t] > moon2[0][t]:
                    moon[1][t] -= 1
                    moon2[1][t] += 1
                elif moon[0][t] < moon2[0][t]:
                    moon[1][t] += 1
                    moon2[1][t] -= 1
        for moon in moons:
            moon[0][t] += moon[1][t]

print(lcm(time[0], lcm(time[1], time[2])))