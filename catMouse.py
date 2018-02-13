#!/bin/python3

import sys

def catAndMouse(x, y, z):
    if abs(z - y) > abs(z - x):
        return "Cat A"
    elif abs(z - y) < abs(z - x):
        return "Cat B"
    else:
        return "Mouse C"
            
                

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        x, y, z = input().strip().split(' ')
        x, y, z = [int(x), int(y), int(z)]
        result = catAndMouse(x, y, z)
        print ("".join(map(str, result)))