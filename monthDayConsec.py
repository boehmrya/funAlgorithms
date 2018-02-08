#!/bin/python3

import sys

# number of diff ways the array s  
# contains m consecutive squares whose integers sum to d.
def solve(n, s, d, m):
    i = 0
    numWays = 0
    while i < len(s):
        j = i
        tempSum = 0
        while j < len(s) and j < (i + m):
            tempSum += s[j]
            j += 1
        if tempSum == d:
            numWays += 1
        i += 1
    return numWays
        
        
        

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)