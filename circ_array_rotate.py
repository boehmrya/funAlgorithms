import sys


def multRotate(k, a):
     '''performs k rotations on list a.
        returns value at index m.'''
     i = 0
     # track number of rotations
     while i < k:
          # perform one rotation on array
          lastItem = a[len(a) - 1]
          a.insert(0, lastItem)
          a.pop()
          i += 1
     return a


n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
a = multRotate(k, a)
for a0 in range(q):
    m = int(input().strip())
    print(a[m])



