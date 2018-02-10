import sys

def bonAppetit(n, k, b, ar):
    aTotal = 0
    i = 0
    while i < len(ar):
        if i != k:
            aTotal += (ar[i] / 2)
        i += 1
    if aTotal == b:
        return "Bon Appetit"
    else:
        return str(int(b - aTotal))

        
n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)