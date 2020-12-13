"""
Python implementation of a Linked List. 

Implements a Node class first, which just is the data + a pointer to the next
thing

The Linked List is then a series of Nodes with a bunch of helper methods for
traversal, etc. 

TODO: implement, append, insert, index, pop
"""

class Node():
  def __init__(self, initdata):
    self.data = initdata
    self.next = None

  def getdata(self):
    return self.data

  def setdata(self, newdata):
    self.data = newdata 
  
  def getnext(self):
    return self.next

  def setnext(self, newnext):
    self.next = newnext

class UnorderedList():
  def __init__(self):
    self.head = None

  def add(self, item):
    i = Node(item)
    i.setnext(self.head)
    self.head = i

  def isEmpty(self):
    return self.head == None

  def size(self):
    count = 0
    tracker = self.head 
    while tracker != None:
      count += 1
      tracker = tracker.getnext()
    return count

  # Returns true if item is found, false otherwise
  def search(self, item):
    tracker = self.head
    found = False
    while tracker != None and not found:
      if tracker.getdata() == item:
        found = True
      else:
        tracker = tracker.getnext()
    return found

  def remove(self, item):
    previous = None
    tracker = self.head
    found = False
    while tracker != None and not found:
      if tracker.getdata() == item:
        found = True
      else:
        previous = tracker
        tracker = tracker.getnext()
    
    if previous == None: # if first item in list, remove head
      self.head = tracker.getnext()
    else: # this method assumes that the item WILL be found
      previous.setnext(tracker.getnext())

l = UnorderedList()
l.add(93)
l.add(54)
l.add(55)
l.add(1234)
l.isEmpty()
print(l.size())
print(l.search(93)) # True
print(l.search(1111)) # False
l.remove(93)
print(l.search(93)) # False
