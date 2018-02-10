#!/bin/python3

import sys

def solve(year):
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 31, 31]
    days = 256
    
    # set number of days in february
    if year < 1918: # use julian calendar
        if year % 4 == 0: # if leap year
            monthDays[1] = 29
    elif year > 1918:
       if year % 400 == 0: # if leap year
            monthDays[1] = 29
       elif ((year % 4 == 0) and (year % 100 != 0)):
            monthDays[1] = 29
    else: # change from julian to gregorian in 1918
        monthDays[1] = 15
    
    # calculate month and day
    i = 0
    while ((days - monthDays[i]) > 0):
        days -= monthDays[i]
        i += 1
        month = i
        
    # set up string to return
    if days < 10:
        days = "0" + str(days)
    if month < 10:
        month = "0" + str(month + 1)
    
    # build full date string in dd.mm.yyyy format
    dateString = str(days) + "." + str(month) + "." + str(year)
    return dateString
        
    
        

year = int(input().strip())
result = solve(year)
print(result)