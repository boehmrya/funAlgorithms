#!/bin/python3

import sys

def divisibleSumPairs(n, k, ar):
    i = 0
    numPairs = 0
    while i < (len(ar) - 1):
        j = i + 1
        while j < len(ar):
            if (ar[i] + ar[j]) % k == 0:
                numPairs += 1
            j += 1
        i += 1
    return numPairs

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)