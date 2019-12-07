import sys

program = [3,8,1001,8,10,8,105,1,0,0,21,38,55,64,81,106,187,268,349,430,99999,3,9,101,2,9,9,1002,9,2,9,101,5,9,9,4,9,99,3,9,102,2,9,9,101,3,9,9,1002,9,4,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,1002,9,5,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,102,2,9,9,1001,9,5,9,102,3,9,9,1001,9,4,9,102,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99]

def get_val(p, m, x):
    if m == 0:
        try:
            return p[x]
        except IndexError:
            print("IndexError: list index out of range:", x)
            exit(1)
    elif m == 1:
        return x

def run(p, buffer, ptr):
    while ptr <= len(p):
        instr = str(p[ptr])
        cmd = int(instr[-2:])
        modes = [0,0,0]
        for i in range(len(instr[:-2])):
            modes[-i-(4-len(instr[:-2]))] = int(instr[:-2][i])

        if cmd == 1:
            p[p[ptr+3]] = get_val(p, modes[0], p[ptr+1]) + get_val(p, modes[1], p[ptr+2])
            ptr += 4
        elif cmd == 2:
            p[p[ptr+3]] = get_val(p, modes[0], p[ptr+1]) * get_val(p, modes[1], p[ptr+2])
            ptr += 4
        elif cmd == 3:
            p[p[ptr+1]] = buffer.pop()
            ptr += 2
        elif cmd == 4:
            buffer.append(get_val(p, modes[0], p[ptr+1]))
            ptr += 2
            return ptr
        elif cmd == 5:
            if get_val(p, modes[0], p[ptr+1]) != 0:
                ptr = get_val(p, modes[1], p[ptr+2])
                continue
            ptr += 3
        elif cmd == 6:
            if get_val(p, modes[0], p[ptr+1]) == 0:
                ptr = get_val(p, modes[1], p[ptr+2])
                continue
            ptr += 3
        elif cmd == 7:
            if get_val(p, modes[0], p[ptr+1]) < get_val(p, modes[1], p[ptr+2]):
                p[p[ptr+3]] = 1
            else:
                p[p[ptr+3]] = 0
            ptr += 4
        elif cmd == 8:
            if get_val(p, modes[0], p[ptr+1]) == get_val(p, modes[1], p[ptr+2]):
                p[p[ptr+3]] = 1
            else:
                p[p[ptr+3]] = 0
            ptr += 4
        elif cmd == 99:
            break
        else:
            print("Something went wrong.")
            exit(1)

max_signal = [0,[]]
for num in range(55555,100000):
    phase = [int(i) for i in str(num)]
    if len(set(range(5)) & set(phase)) > 0 or len(set(phase)) != len(phase):
        continue
    ptrs = [0,0,0,0,0]
    prgrms = [list(program) for i in range(5)]
    buf = [0]
    for i in range(5):
        buf.append(phase[i])
        res = run(prgrms[i], buf, ptrs[i])
        if res is not None:
            ptrs[i] = res
        
    halt = False
    while not halt:
        for i in range(5):
            res = run(prgrms[i], buf, ptrs[i])
            if res is not None:
                ptrs[i] = res
            else:
                if i == 4:
                    halt = True
    if buf[0] > max_signal[0]:
        max_signal = [buf[0], phase]

print(max_signal)