signal = "59750530221324194853012320069589312027523989854830232144164799228029162830477472078089790749906142587998642764059439173975199276254972017316624772614925079238407309384923979338502430726930592959991878698412537971672558832588540600963437409230550897544434635267172603132396722812334366528344715912756154006039512272491073906389218927420387151599044435060075148142946789007756800733869891008058075303490106699737554949348715600795187032293436328810969288892220127730287766004467730818489269295982526297430971411865028098708555709525646237713045259603175397623654950719275982134690893685598734136409536436003548128411943963263336042840301380655801969822"
test1 = "12345678"
test2 = "80871224585914546619083218645595"
test3 = "19617804207202209144916044189917"
test4 = "69317163492948606335995924319873"
test5 = "03036732577212944063491565474664"
test6 = "02935109699940807407585447034323"
test7 = "03081770884921959731165446850517"

def phase(s):
    res = []
    back_sum = 0
    for i in range(len(s)):
        sum = 0
        for j in range(i, len(s)):
            pat_mult = i+1
            pat_i = (j+1)%(4*pat_mult)
            if pat_i < pat_mult:
                k = 0
            elif pat_i < 2*pat_mult:
                k = 1
            elif pat_i < 3*pat_mult:
                k = 0
            elif pat_i < 4*pat_mult:
                k = -1
            sum += k*s[j]
        res.append(abs(sum)%10)
    return res

def n_phases(s, n):
    for i in range(n):
        s = phase(s)
        print("Phase:", i+1, end="\r")
    return "".join(map(str, s[:8]))

# Works if off > len(s)/2, 
# since the second half is independant of the first half
def phase2(s, off):
    back_sum = 0
    for i in reversed(range(off, len(s))):
        back_sum += s[i]
        s[i] = back_sum%10

def n_phases2(s, n, off):
    for i in range(n):
        phase2(s, off)
        print("Phase:", i+1, end="\r")
    return "".join(map(str, s[off:off+8]))

def main(s):
    int_ls = [int(c) for c in s]
    part1 = n_phases(list(int_ls), 100)
    print("Part 1:", part1)
    offset = int(s[:7])
    part2 = n_phases2((list(int_ls)*10000), 100, offset)
    print("Part 2:", part2)

main(signal)

# Input: 123789
# Output[3]: (7+8+9)%10
# Output[4]: (8+9)%10
# Output[5]: (9)%10