import time
import random

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
      midpoint = (first + last)//2
      if alist[midpoint] == item:
        found = True
      else:
	      if item < alist[midpoint]:
	        last = midpoint-1
	      else:
	        first = midpoint+1
	      return found

# Recursive
def binarySearch2(alist, item):
  if len(alist) == 0:
      return False
  else:
      midpoint = len(alist)//2
      if alist[midpoint]==item:
        return True
      else:
        if item<alist[midpoint]:
            return binarySearch(alist[:midpoint],item)
        else:
            return binarySearch(alist[midpoint+1:],item)
"""
We have two implementations of binary search, a recursive one and an iterative
one. Idea is to benchmark these against an ordered list, so I picked a
Fibonacci sequence as an example. 
"""

# generate fibonnacci

fib = [1]
i=1
while i<10000000000:
  fib.append(i)
  i = i + fib[-2]

s = len(fib)

iterativeTimes = []
recursiveTimes = []

for i in range(1000):
  k = fib[random.randint(0,s-1)]
  
  start1=time.time()
  binarySearch(fib, k)
  end1=time.time()
  
  t = (end1-start1)*1000
  iterativeTimes.append(t)

for i in range(1000):
  k = fib[random.randint(0,s-1)]
  
  start2=time.time()
  binarySearch2(fib, k)
  end2=time.time()
  
  t = (end2-start2)*1000
  recursiveTimes.append(t)

def Average(lst):
  return sum(lst) / len(lst)

print("Average for iteratives: %f" % Average(iterativeTimes))
print("Average for recursives: %f" % Average(recursiveTimes))

# Recursive is slower than iterative by ~2x. I think this is because the
# recursive implementation is using Python's "slice" operator, which is O(k). To
# prove this, let's try a third implementation of binary search that is
# recursive but doesn't use slice. 

def binarySearch3(alist, item, *args):
  if args:
    if len(alist[args[0]:args[1]]) == 0:
      return False
  if len(alist) == 0:
    return False
  else:
      if args:
        start = args[0]
        end = args[1]
        midpoint = (start+end)//2
      else:
        start = 0
        end = len(alist)-1
        midpoint = (start+end)//2
      if alist[midpoint]==item:
        return True
      else:
        if item<alist[midpoint]:
            return binarySearch3(alist,item,start,midpoint-1)
        else:
            return binarySearch3(alist,item,midpoint+1,end)

recursiveTimes2 = []

for i in range(1000):
  k = fib[random.randint(0,s-1)]
  
  start3=time.time()
  binarySearch3(fib, k)
  end3=time.time()
  
  t = (end3-start3)*1000
  recursiveTimes2.append(t)

print("Average for recursives 2: %f" % Average(recursiveTimes2))

# This implementation of the recursive binary search beats the other two!
