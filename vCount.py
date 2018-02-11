#!/bin/python3

import sys

def countingValleys(n, s):
    currentLevel = 0 # sea level
    numValleys = 0 # track number of valleys
    belowSeaLevel = False
    for step in s:
        if step == "U": 
            currentLevel += 1
        else:
            currentLevel -= 1
        if (currentLevel < 0) and (belowSeaLevel == False):
            belowSeaLevel = True
        elif (currentLevel >= 0) and (belowSeaLevel == True):
            belowSeaLevel = False
            numValleys += 1
    return numValleys
        
        
        
        
        
    return numValleys
        

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)