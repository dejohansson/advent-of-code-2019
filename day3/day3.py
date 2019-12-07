import numpy as np

def load_lines(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
        return lines[0].split(","), lines[1].split(",")

def plt(b, line, id, start):
    step_count = 0
    inter_step = {}
    min_dist = np.inf
    x = start[0]; y = start[1]
    for m in line:
        direction = m[0]
        if direction == "R":
            step = lambda a, b : (a+1, b)
        elif direction == "L":
            step = lambda a, b : (a-1, b)
        elif direction == "U":
            step = lambda a, b : (a, b+1)
        elif direction == "D":
            step = lambda a, b : (a, b-1)
        
        for i in range(int(m[1:])):
            x, y = step(x, y)
            step_count += 1
            if b[x,y] == 0:
                b[x,y] = id
            elif b[x,y] == id:
                pass
            else:
                b[x,y] = 99
                if (x, y) not in inter_step:
                    inter_step[(x, y)] = step_count
                dist = abs(x-start[0]) + abs(y-start[1])
                if dist < min_dist:
                    min_dist = dist
                
    return min_dist, inter_step

def find_shortest(l1, l2, b_size):
    board = np.zeros((b_size, b_size)).astype(np.uint8)
    dist1, s1 = plt(board, l1, 1, (b_size//2, b_size//2))
    dist2, s2 = plt(board, l2, 2, (b_size//2, b_size//2))
    dist1, s1 = plt(board, l1, 1, (b_size//2, b_size//2))

    shortest = np.inf
    for (k, v) in s1.items():
        steps = v + s2[k]
        if steps < shortest:
            shortest = steps
    return dist2, shortest

size = 20000

line1, line2 = load_lines("day3/lines.txt")
print(find_shortest(line1, line2, size))

line3 = ["R75","D30","R83","U83","L12","D49","R71","U7","L72"]
line4 = ["U62","R66","U55","R34","D71","R55","D58","R83"]
print(find_shortest(line3, line4, size))

line5 = ["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"]
line6 = ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"]
print(find_shortest(line5, line6, size))

"""board = np.zeros((size, size)).astype(np.uint8)
l1, l2 = load_lines("day3/lines.txt")

print(plt(board, l1, 1, (size//2, size//2)))
print(plt(board, l2, 2, (size//2, size//2)))

board = np.zeros((size, size)).astype(np.uint8)
l3 = ["R75","D30","R83","U83","L12","D49","R71","U7","L72"]
l4 = ["U62","R66","U55","R34","D71","R55","D58","R83"]

print(plt(board, l3, 1, (size//2, size//2)))
print(plt(board, l4, 2, (size//2, size//2)))

board = np.zeros((size, size)).astype(np.uint8)
l5 = ["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"]
l6 = ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"]

print(plt(board, l5, 1, (size//2, size//2)))
print(plt(board, l6, 2, (size//2, size//2))) """

