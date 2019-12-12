"""moons = [[[1, 4, 4], [0, 0, 0]],
        [[-4, -1, 19], [0, 0, 0]],
        [[-15, -14, 12], [0, 0, 0]],
        [[-17, 1, 10], [0, 0, 0]],]"""

moons = [[[-8, -10, 0], [0, 0, 0]],
        [[5, 5, 10], [0, 0, 0]],
        [[2, -7, 3], [0, 0, 0]],
        [[9, -8, -3], [0, 0, 0]],]

"""moons = [[[-1,0,2], [0, 0, 0]],
        [[2,-10,-7], [0, 0, 0]],
        [[4,-8,8], [0, 0, 0]],
        [[3,5,-1], [0, 0, 0]],]"""

"""for s in range(1000):
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
print(energy)"""

points = []
pt = tuple([ (tuple(moon[0]), tuple(moon[1])) for moon in moons])
points.append(pt)
                #4686774924
                #100000
                #123400000     
for num in range(10000000000):
    if num%100000 == 0:
        print(num)

    pt = tuple([ (tuple(moon[0]), tuple(moon[1])) for moon in moons])
    if pt in points and num != 0:
        print(num)
        break
    

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