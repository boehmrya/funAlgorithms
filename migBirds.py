#!/bin/python3

import sys

def migratoryBirds(n, ar):
    freq = [0, 0, 0, 0, 0] # holds frequencies for 1 - 5
    
    # build frequencies
    for bird in ar:
        freq[bird - 1] += 1
           
    # get max bird type
    maxBirdCount = freq[0]
    maxBird = 0
    i = 0
    while i < len(freq):
        if freq[i] > maxBirdCount:
            maxBirdCount = freq[i]
            maxBird = i
        i += 1
    return (maxBird + 1)
        

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)