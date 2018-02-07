#!/bin/python3

import sys

def breakingRecords(score):
    numHigh = 0
    numLow = 0
    maxHigh = score[0]
    maxLow = score[0]
    for s in score:
        if s > maxHigh:
            numHigh += 1
            maxHigh = s
        elif s < maxLow:
            numLow += 1
            maxLow = s
    return [numHigh, numLow]

if __name__ == "__main__":
    n = int(input().strip())
    score = list(map(int, input().strip().split(' ')))
    result = breakingRecords(score)
    print (" ".join(map(str, result)))