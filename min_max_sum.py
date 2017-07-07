
import sys

a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

arr = [a, b, c, d, e]
arr.sort()
min = 0
max = 0
i = 0
while i < (len(arr) - 1):
     min += arr[i]
     i += 1

j = 1
while j < len(arr):
     max += arr[j]
     j += 1

print(str(min) + " " + str(max))
