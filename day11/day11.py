import numpy as np

class IntCodePc:
    def __init__(self, program):
        self.p = list(program) + [0]*10000
        self.ptr = 0
        self.rel_base = 0
        self.modes = []

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
    
    def run(self, in_code):
        while self.ptr <= len(self.p):
            #print("pp:", self.ptr)
            #print(self.p[:150])
            instr = str(self.p[self.ptr])
            #print("i:", instr)
            cmd = int(instr[-2:])
            self.modes = [int(i) for i in reversed(instr[:-2])] + ([0]*(3-len(instr[:-2])))

            if cmd == 1:
                self.set_val(3, self.get_val(1) + self.get_val(2))
                self.ptr += 4
            elif cmd == 2:
                self.set_val(3, self.get_val(1) * self.get_val(2))
                self.ptr += 4
            elif cmd == 3:
                #print(in_code)
                self.set_val(1, in_code)
                self.ptr += 2
            elif cmd == 4:
                #print("Output:", self.get_val(1))
                return_val = self.get_val(1)
                self.ptr += 2
                #print(self.p[:150])
                #print()
                #print(self.modes[0])
                #print(self.p[self.ptr + 1])
                #print("v:", self.get_val(1))
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
                return 99
            else:
                print("Something went wrong.")
                exit(1)
            #print(self.p[:150])
            #print()
hull = np.zeros((1000, 1000), dtype=np.uint8)
program = [3,8,1005,8,299,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,28,1006,0,85,1,106,14,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,58,1,1109,15,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,1002,8,1,84,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,105,1006,0,48,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,130,1006,0,46,1,1001,17,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,160,2,109,20,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,185,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,207,1006,0,89,2,1002,6,10,1,1007,0,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,101,0,8,241,2,4,14,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,101,0,8,267,1,1107,8,10,1,109,16,10,2,1107,4,10,101,1,9,9,1007,9,1003,10,1005,10,15,99,109,621,104,0,104,1,21101,0,387239486208,1,21102,316,1,0,1106,0,420,21101,0,936994976664,1,21102,327,1,0,1105,1,420,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,1,29192457307,1,21102,1,374,0,1106,0,420,21101,0,3450965211,1,21101,0,385,0,1106,0,420,3,10,104,0,104,0,3,10,104,0,104,0,21102,1,837901103972,1,21101,408,0,0,1106,0,420,21102,867965752164,1,1,21101,0,419,0,1105,1,420,99,109,2,22102,1,-1,1,21102,40,1,2,21102,451,1,3,21102,1,441,0,1106,0,484,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,446,447,462,4,0,1001,446,1,446,108,4,446,10,1006,10,478,1102,0,1,446,109,-2,2105,1,0,0,109,4,1201,-1,0,483,1207,-3,0,10,1006,10,501,21101,0,0,-3,22101,0,-3,1,22102,1,-2,2,21101,1,0,3,21101,520,0,0,1106,0,525,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,548,2207,-4,-2,10,1006,10,548,21201,-4,0,-4,1105,1,616,22101,0,-4,1,21201,-3,-1,2,21202,-2,2,3,21101,0,567,0,1106,0,525,22101,0,1,-4,21101,1,0,-1,2207,-4,-2,10,1006,10,586,21102,1,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,608,21202,-1,1,1,21102,608,1,0,106,0,483,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0]
robot = IntCodePc(program)
x = 500
y = 500
direction = "U"

panels = []
while True:
    #print("p:", robot.ptr)
    print(x, y)
    """if hull[x, y] != 1 and hull[x, y] != 0:
        print("hull")
        print(hull[x, y])
        exit()"""
    hull_color = hull[x, y]
    new_color = robot.run(hull_color)
    """if new_color != 0 and new_color != 1:
        print(new_color)
        exit()"""
    if new_color == 99:
        break
    hull[x, y] = new_color
    rotation = robot.run(None)
    """if rotation != 0 and rotation != 1:
        print("p:", robot.ptr)
        print("rotation")
        print(rotation)
        exit()"""
    if rotation == 99:
        break

    if (x, y) not in panels:
        print(len(panels))
        panels.append((x,y))

    if direction == "R" and rotation == 0:
        direction = "U"
    elif direction == "R" and rotation == 1:
        direction = "D"
    if direction == "L" and rotation == 0:
        direction = "D"
    elif direction == "L" and rotation == 1:
        direction = "U"
    if direction == "U" and rotation == 0:
        direction = "L"
    elif direction == "U" and rotation == 1:
        direction = "R"
    if direction == "D" and rotation == 0:
        direction = "R"
    elif direction == "D" and rotation == 1:
        direction = "L"

    if direction == "R":
        step = lambda a, b : (a+1, b)
    elif direction == "L":
        step = lambda a, b : (a-1, b)
    elif direction == "U":
        step = lambda a, b : (a, b+1)
    elif direction == "D":
        step = lambda a, b : (a, b-1)
    x, y = step(x, y)

print("Panels: ", len(panels))