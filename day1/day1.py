import numpy as np
import os
import sys

def extra_fuel(x):
    if int(x/3)-2 > 0:
        return int(x/3)-2 + extra_fuel(int(x/3)-2)
    else:
        return 0

test = [12, 14, 1969, 100756]

with open("Day1/mass.txt", "r") as f:
    mass = f.read().split("\n")

fuel = ((np.array(mass).astype(int)/3).astype(int)-2).sum()

total_fuel = 0

for m in mass:
    total_fuel += extra_fuel(int(m))