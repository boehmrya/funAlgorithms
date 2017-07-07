
import sys

x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]


jumps = 1
miss = True

while jumps < 10000:
     k1 = x1 + (jumps * v1)
     k2 = x2 + (jumps * v2)
     if k1 == k2:
          miss = False
     jumps += 1

if miss == True:
     print("NO")
else:
     print("YES")

