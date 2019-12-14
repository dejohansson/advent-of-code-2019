import math

def load_reactions(file_name):
    res = {}
    with open(file_name, "r") as f:
        lines = f.read().split("\n")
    for line in lines:
        line = line.split("=>")
        out = line[1].split(" ")
        res[out[2]] = (int(out[1]), [(chem.split(" ")[1], int(chem.split(" ")[0])) for chem in line[0].split(", ")])
    return res

def done(d):
    for v in d.values():
        if v > 0:
            return False
    return True

def get_num_ore(f):
    required = {"FUEL": f}
    ore_count = 0
    while not done(required):
        for chem, qt in list(required.items()):
            if qt > 0:
                mult = math.ceil(qt/reactions[chem][0])
                for req in reactions[chem][1]:
                    if req[0] == "ORE":
                        ore_count += req[1]*mult
                    else:
                        if req[0] in required:
                            required[req[0]] += req[1]*mult
                        else:          
                            required[req[0]] = req[1]*mult
                required[chem] -= reactions[chem][0]*mult
    return ore_count

reactions = load_reactions("day14/reactions.txt")

print("Part 1 Ore Amount:", get_num_ore(1))

max_ore = 1000000000000
high = max_ore
low = 1
while high-low > 1:
    fuel_n = (high+low)//2
    ore_n = get_num_ore(fuel_n)
    if ore_n > max_ore:
        high = fuel_n
    else:
        low = fuel_n
    #print(fuel_n, ore_n, high, low, fuel_n)
print("Part 2 Fuel Amount:", fuel_n)
