import sys

h = [int(h_temp) for h_temp in input().strip().split(' ')]
word = input().strip()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
maxHeight = 0

for ch in word:
     index = alphabet.find(ch)
     height = h[index]
     if height > maxHeight:
          maxHeight = height

wordArea = (len(word) * maxHeight)
print(wordArea)
     
