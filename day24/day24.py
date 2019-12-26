start = """\
..###
##...
#...#
#.#.#
.#.#."""

test = """\
....#
#..#.
#..##
..#..
#...."""

current = tuple([tuple([c for c in line]) for line in start.split("\n")])
states = {current}

while True:
    new_state = []
    for i, row in enumerate(current):
        new_row = []
        for j, val in enumerate(row):
            bug_count = 0
            for a, b in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                try:
                    if a >= 0 and b >= 0 and current[a][b] == "#": bug_count += 1
                except: pass
            if val == "#" and bug_count != 1:
                new_row.append(".")
            elif val == "." and (bug_count == 1 or bug_count == 2):
                new_row.append("#")
            else:
                new_row.append(val)
        new_state.append(tuple(new_row))
    current = tuple(new_state)
    if current in states: break
    else: states.add(current)

biodiv = 0
for i, val in enumerate([v for l in current for v in l]):
    if val == "#":
        biodiv += 2**i
print("Biodiversity:", biodiv)