def pass_check(x):
    double = False
    prev = -1
    for i in str(x):
        if int(i) == prev:
            double = True
        elif int(i) < prev:
            return False
        prev = int(i)
    return double

print(pass_check(111111))
print(pass_check(223450))
print(pass_check(123789))

correct = 0

for i in range(130254, (678275)+1):
    if pass_check(i):
        correct += 1

print(correct)

def pass_check2(x):
    double = False
    seq = str(x)

    for i in range(3, 6):
        sub_seq = seq[i-3:i+1]
        prev = 0
        for j in sub_seq:
            if int(j) < prev:
                return False
            prev = int(j)
        if sub_seq[0] != sub_seq[1] and sub_seq[1] == sub_seq[2] and sub_seq[2] != sub_seq[3]:
            double = True
        elif i == 3 and sub_seq[0] == sub_seq[1] and sub_seq[1] != sub_seq[2]:
            double = True
        elif i == 5 and sub_seq[1] != sub_seq[2] and sub_seq[2] == sub_seq[3]:
            double = True
    return double



print(pass_check2(112233))
print(pass_check2(123444))
print(pass_check2(111122))

correct2 = 0

for i in range(130254, (678275)+1):
    if pass_check2(i):
        correct2 += 1

print(correct2)