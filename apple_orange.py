
import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

appleTreeDist = s - a
orangeTreeDist = b - t
houseApples = 0
houseOranges = 0

for d in apple:
     loc = a + d
     if (loc >= s and loc <= t):
          houseApples += 1

for d in orange:
     loc = b + d
     if (loc >= s and loc <= t):
          houseOranges += 1

print(houseApples)
print(houseOranges)
          
