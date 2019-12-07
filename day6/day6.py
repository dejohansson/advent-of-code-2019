import math

def load_orbits(file_name):
    with open(file_name, "r") as f:
        lines = f.read().split("\n")
        return [tuple(line.split(")")) for line in lines]
            
class Object:
    def __init__(self, name, orbits):
        self.name = name
        self.orbits = orbits
    
    def get_distances(self):
        if self.orbits:
            dist = self.orbits.get_distances()
            for key in dist.keys():
                dist[key] += 1
            dist[self.orbits.name] = 1
        else:
            dist = {}
        return dist

def total_orbits(obj):
    if obj.orbits:
        return 1+total_orbits(obj.orbits)
    return 0

orbits = load_orbits("day6/orbits.txt")
test_orbits = load_orbits("day6/test.txt")

orbit_dict = {}

for o in orbits:
    if o[0] not in orbit_dict:
        orbit_dict[o[0]] = Object(o[0], None)
    if o[1] not in orbit_dict:
        orbit_dict[o[1]] = Object(o[1], None)
    orbit_dict[o[1]].orbits = orbit_dict[o[0]]

orbit_num = 0
for o in orbit_dict.values():
    orbit_num += total_orbits(o)

print(orbit_num)

you = orbit_dict["YOU"].get_distances()
san = orbit_dict["SAN"].get_distances()
inter = you.keys() & san.keys()

closest = math.inf
for key in inter:
    dist = you[key] + san[key] - 2
    if dist < closest:
        closest = dist

print(closest)