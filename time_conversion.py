import sys

time = input().strip()
numTime = time[:-2] #numeric time with colons
timeOfDay = time[-2] + time[-1] #am or pm
timeList = numTime.split(':')
numHours = int(timeList[0])

# make the conversion
if timeOfDay == 'PM' and numHours < 12:
     numHours = numHours + 12
elif timeOfDay == 'AM':
     numHours = numHours % 12

# prepend zero for single digit numbers
timeList[0] = str(numHours)
if len(timeList[0]) < 2:
    timeList[0] = ('0' + timeList[0])
militaryTime = ':'.join(timeList)
print(militaryTime)
     
