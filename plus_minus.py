import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

posTotal = 0
negTotal = 0
zeroTotal = 0
numTotal = len(arr)

for num in arr:
     if num > 0:
          posTotal += 1
     elif num < 0:
          negTotal += 1
     else:
          zeroTotal += 1

posFract = posTotal / numTotal
negFract = negTotal / numTotal
zeroFract = zeroTotal / numTotal

print("{:.6f}".format(posFract))
print("{:.6f}".format(negFract))
print("{:.6f}".format(zeroFract))
