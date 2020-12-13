import time
import random

def sequentialSearch(item, ints):
  for i in ints:
    if i == item:
      print(item)
      return True
    else:
      pass
  return False

def binarySearch(item, ints):
  if len(ints) == 0: 
    return False
  start = ints[0]
  end = ints[-1]
  midpoint = len(ints)//2
  if ints[midpoint] == item:
    print(item)
    return True
  else:
    if ints[midpoint] < item:
      return binarySearch(item, ints[midpoint+1:])
    if ints[midpoint] > item:
      return binarySearch(item, ints[:midpoint])

# Benchmarking

for listSize in range(1000,1100001,100000):
  randlist = random.sample(range(0,listSize), listSize)
  i = randlist[random.randint(0,listSize)]
  start1 = time.time()
  sequentialSearch(i, randlist)
  end1=time.time()
  print("Sequential search took %f ms to search size %d" % ((end1-start1)*1000,
  listSize))

for listSize in range(1000,1100001,100000):
  randlist = random.sample(range(0,listSize), listSize)
  i = randlist[random.randint(0,listSize)]
  start2 = time.time()
  binarySearch(i, randlist)
  end2 = time.time()
  print("Binary search took %f ms to search size %d" % ((end2-start2)*1000, listSize))
