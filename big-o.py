"""
Compare two implementations of finding the minimum of a list.
"""

import time
from random import randrange

# Very inefficient. O(n^2). 
def findMin1(lst):
  min = 0
  for char in lst:
    min = char
    for c in lst:
      if c < char:
        min = c
      else:
        pass
  return min

# Pretty efficient. O(n). 
def findMin2(lst):
  min = lst[0]
  for char in lst:
    if char < min:
      min = char
  return min

# Test
print(findMin1([5,4,2,1,0]))
print(findMin2([5,4,2,1,0]))

# Benchmark.
for listSize in range(1000, 10001, 1000):
  alist=[randrange(100000) for x in range(listSize)]
  start1 = time.time()
  print(findMin1(alist))
  end1=time.time()
  print("1. size: %d time: %f" % (listSize, end1-start1))

for listSize in range(1000,10001,1000):
  start2 = time.time()
  print(findMin2(alist))
  end2=time.time()
  print("2. size: %d time: %f" % (listSize, end2-start2))
