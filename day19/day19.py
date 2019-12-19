class IntCodePc:
    def __init__(self, program):
        self.p = list(program)
        self.ORIGINAL_PROGRAM = list(program)
        self.ptr = 0
        self.rel_base = 0
        self.modes = []
        self.halted = False
        self.inputs = []

    def reset(self, program=None):
        if program is None: program = self.ORIGINAL_PROGRAM
        self.p = list(program)
        self.ptr = 0
        self.rel_base = 0
        self.modes = []
        self.halted = False
        self.inputs = []

    def set_val(self, offset, val):
        if self.modes[offset-1] == 0:
            index = self.p[self.ptr + offset]
        elif self.modes[offset-1] == 2:
            index = self.rel_base + self.p[self.ptr + offset]
        while index > len(self.p)-1:
            self.p.append(0)
        self.p[index] = val

    def get_val(self, offset):
        if self.modes[offset-1] == 0:
            try:
                return self.p[self.p[self.ptr + offset]]
            except IndexError:
                print("IndexError: list index out of range:", self.p[self.rel_base + self.ptr + offset])
                exit(1)
        elif self.modes[offset-1] == 1:
            return self.p[self.ptr + offset]
        elif self.modes[offset-1] == 2:
            try:
                return self.p[self.rel_base + self.p[self.ptr + offset]]
            except IndexError:
                print("IndexError: list index out of range:", self.p[self.rel_base + self.ptr + offset])
                exit(1)
    
    def run(self, input_list):
        if input_list is not None:
            self.inputs += input_list
        while self.ptr <= len(self.p):
            instr = str(self.p[self.ptr])
            cmd = int(instr[-2:])
            self.modes = [int(i) for i in reversed(instr[:-2])] + ([0]*(3-len(instr[:-2])))

            if cmd == 1:
                self.set_val(3, self.get_val(1) + self.get_val(2))
                self.ptr += 4
            elif cmd == 2:
                self.set_val(3, self.get_val(1) * self.get_val(2))
                self.ptr += 4
            elif cmd == 3:
                if len(self.inputs) == 0:
                    print("Empty input")
                    exit(1)
                self.set_val(1, self.inputs.pop(0))
                self.ptr += 2
            elif cmd == 4:
                return_val = self.get_val(1)
                self.ptr += 2
                return return_val
            elif cmd == 5:
                if self.get_val(1) != 0:
                    self.ptr = self.get_val(2)
                else:
                    self.ptr += 3
            elif cmd == 6:
                if self.get_val(1) == 0:
                    self.ptr = self.get_val(2)
                else:
                    self.ptr += 3
            elif cmd == 7:
                if self.get_val(1) < self.get_val(2):
                    self.set_val(3, 1)
                else:
                    self.set_val(3, 0)
                self.ptr += 4
            elif cmd == 8:
                if self.get_val(1) == self.get_val(2):
                    self.set_val(3, 1)
                else:
                    self.set_val(3, 0)
                self.ptr += 4
            elif cmd == 9:
                self.rel_base += self.get_val(1)
                self.ptr += 2
            elif cmd == 99:
                self.halted = True
                print("halted")
                return 99
            else:
                print("Something went wrong.")
                exit(1)

program = [109,424,203,1,21101,0,11,0,1105,1,282,21101,18,0,0,1105,1,259,1202,1,1,221,203,1,21102,1,31,0,1106,0,282,21102,38,1,0,1106,0,259,21002,23,1,2,22102,1,1,3,21102,1,1,1,21102,1,57,0,1105,1,303,2102,1,1,222,20101,0,221,3,21001,221,0,2,21102,259,1,1,21102,1,80,0,1106,0,225,21102,62,1,2,21101,91,0,0,1105,1,303,2101,0,1,223,21001,222,0,4,21101,0,259,3,21101,0,225,2,21101,0,225,1,21101,0,118,0,1105,1,225,20102,1,222,3,21101,94,0,2,21102,133,1,0,1105,1,303,21202,1,-1,1,22001,223,1,1,21101,0,148,0,1105,1,259,1202,1,1,223,20101,0,221,4,21001,222,0,3,21102,17,1,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21101,195,0,0,105,1,109,20207,1,223,2,20101,0,23,1,21102,-1,1,3,21101,214,0,0,1106,0,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,2101,0,-4,249,22102,1,-3,1,22101,0,-2,2,21201,-1,0,3,21102,1,250,0,1106,0,225,22101,0,1,-4,109,-5,2105,1,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22101,0,-2,-2,109,-3,2106,0,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,21201,-2,0,3,21101,343,0,0,1106,0,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,22102,1,-4,1,21102,384,1,0,1105,1,303,1105,1,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,21201,1,0,-4,109,-5,2105,1,0]
drone_system = IntCodePc(program)

grid_size = 50
grid = []
points = 0
for y in range(grid_size):
    grid.append([])
    for x in range(grid_size):
        output = drone_system.run([x, y])
        if output == 1:
            points += 1
            grid[y].append("#")
        else:
            grid[y].append(".")
        drone_system.reset()
for line in grid:
    print("".join(line))
print("Part 1:", points)

def get_square_pos(size, pr, max_depth):
    line_start = {}
    for y in range(max_depth):
        print("Y:", y, end="\r")
        for x in range(line_start.get((y-1), 0), max_depth):
            output = pr.run([x, y])
            pr.reset()
            if output == 1:
                if y not in line_start: 
                    line_start[y] = x
                    x += size-1
                dx = pr.run([x+size-1, y])
                pr.reset()
                if dx != 1: break
                dy = pr.run([x, y+size-1])
                pr.reset()
                if dy != 1: continue
                return x,y

x, y = get_square_pos(100, drone_system, 1000)
print("Part 2:", x*10000+y)