
import sys

n = int(input().strip())

i = 1
while i <= n:
     hashes = i * '#'
     spaces = (n - i) * ' '
     line = spaces + hashes
     print(line)
     i += 1
