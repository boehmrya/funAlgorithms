
import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]

largest = max(a)
factors = []

# first gather list of elements that all elements in A
# are a factor of.
count = largest
while count <= 1000000:
     factorStatus = True
     for elem in a:
          if count % elem != 0:
               factorStatus = False
     if factorStatus == True:
          factors.append(count)
     count += 1


# go back through the list created above, and check if
# each is a factor of all elements in B.
between = []
for elem in factors:
     factorStatus = True
     for item in b:
          if item % elem != 0:
               factorStatus = False
     if factorStatus == True:
          between.append(elem)


# output the number of factors between the two sets
print(len(between))

               
