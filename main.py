# DECLARING THE VALUE OF n

import numpy as np
n = int(input("Enter the value of n : "))
print("Value of n =", n)

# GETTING THE INPUTS

InputVal = {}
for i in range(1, n+1):
    val = int(input(f"Enter the value no {i} : "))
    try:
        InputVal[val] += 1
    except:
        InputVal[val] = 1
print(f"{i} Values Collected Successfully")

# FINDING MEAN

mean = 0
for key, val in InputVal.items():
    mean += key*(val/n)
print(f"Mean = {mean:.3f}")

# FINDING VARIANCE

ex2 = 0
for key, val in InputVal.items():
    ex2 += ((key**2) * val/n)
var = ex2 - mean**2
print(f"Variance : {var:.3f}")

# FINDING STANDARD DEVIATION

from math import sqrt
sdtDeviation = sqrt(var)
print(f"Standard Deviation = {sdtDeviation:.3f}")