

#!/bin/python3

import sys

def solve(grades):
    newGrades = []
    for grade in grades:
        if grade < 38:
            newGrades.append(grade)
        else:
            fromBelow = grade % 5 # diff between num and next lowest multiple of 5
            toAbove = 5 - fromBelow # amount to add if we need to round up
            if (grade % 5) > 2:
                newGrades.append(grade + toAbove) # round up to next muliple of 5
            else:
                newGrades.append(grade) # no rounding
    return newGrades
    

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))