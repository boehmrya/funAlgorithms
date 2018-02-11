#!/bin/python3

import sys

def solve(n, p):
    numTurns = 0
    
    # determine the starting page
    if ((n - p) > (p - 1)):
        startPage = 1
        currentPage = startPage
        while (currentPage < p):
            currentPage += 2
            numTurns += 1
    else:
        startPage = n
        currentPage = startPage
        while (currentPage > p):
            # if last page and number of pages is odd
            if (currentPage == n) and (n % 2 != 0) and ((n - p) <= 1):
                break;
            else:
                if (currentPage == n) and (n % 2 != 0): # if last page and last page is odd, subtract 3
                    currentPage -= 3
                else:
                    currentPage -= 2
            numTurns += 1
     
    return numTurns    
    

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)