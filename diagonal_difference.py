
import sys
import math

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

# primary diagonal
firstSum = 0
i = 0
j = 0
while i < len(a):
     firstSum += a[i][j]
     i += 1
     j += 1

# secondary diagonal
secondSum = 0
i = len(a) - 1
j = 0
while i >= 0:
     secondSum += a[i][j]
     i -= 1
     j += 1

print(int(math.fabs(firstSum - secondSum)))
