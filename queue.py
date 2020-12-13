"""
Implements a Queue in Python
URL: https://runestone.academy/runestone/books/published/pythonds/BasicDS/ImplementingaQueueinPython.html
"""

class Queue():
  def __init__(self, *args):
    self.data = []
    for a in args:
      self.data.append(a)
  
  def show(self):
    print(self.data)

  def enqueue(self, item):
    # The 0-index is the rear of the queue
    self.data.insert(0, item)

  def dequeue(self):
    # Removes the item at the front of the queue (i.e. the end of the array.)
    return self.data.pop()

  def isEmpty(self):
    return self.data == []

  def size(self):
    return len(self.data)

a = Queue()
a.enqueue("wtf")
a.show()
print(a.dequeue())
