#!/bin/python3

import sys

def sockMerchant(n, ar):
    freq = 101 * [0]
    # build list of color frequencies
    for sock in ar:
        freq[sock] += 1
    
    # see how many pairs are of each
    numPairs = 0
    for color in freq:
        numPairs += (color // 2)
    
    return numPairs
    
    

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)