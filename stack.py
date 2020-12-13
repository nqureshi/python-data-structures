"""
Implements a simple Stack class in Python. 
URL: https://runestone.academy/runestone/books/published/pythonds/BasicDS/ImplementingaStackinPython.html

Applications of the stack:
1) Algorithm to a reverse a string (simplest)
2) Algorithm to detect if parantheses are balanced
- Read left -> right
  - Balanced is 'true' to start
  - If it's "(", add it to the stack
  - If it's ")", pop the stack
  - If your stack is empty and you get a ")", not balanced (exit)
  - If your stack is empty and you're done, you're balanced (exit)  

"""

class Stack():
  def __init__(self, *args):
    self.data = []
    for a in args:
      self.data.append(a)

  def show(self):
    print(self.data)

  def push(self, item):
    self.data.append(item)

  def pop(self):
    return self.data.pop()

  def peek(self):
    return self.data[-1]

  def isEmpty(self):
    if not self.data:
      return True
    else:
      return False

  def size(self):
    return len(self.data)

# Basic stack application: reverse a string
def revstring(mystr):
  x = Stack()
  for a in mystr:
    x.push(a)
  l1 = []
  for a in mystr:
    l1.append(x.pop())
  return ''.join(l1)

def parensCheck(parens):
  checker = Stack()
  balanced = True
  for c in parens:
    if c == "(":
      checker.push(c)
    elif c == ")":
      if checker.isEmpty():
        balanced = False
        return balanced
      checker.pop()
  if checker.isEmpty():
    return balanced
  else:
    balanced = False
    return balanced

# Test basic stack functionality
v = Stack()
v.show()
s = Stack(2, True, "dog")
s.show()
print("Test push...")
v.push("cat")
v.show()
print("Test pop...")
print(v.pop()) # expects "cat"
v.push("cat2")
print(v.peek()) # expects "cat2"
print(v.isEmpty()) # expects False
print(v.pop()) # expects "cat2"
print(v.isEmpty()) # expects True
print(s.size()) # expects 3

# Test reverse string algorithm
test = "radiohead"
print(revstring(test))

# Test parens balancing algorithm
p1 = "((()))"
p2 = "())("
p3 = "((()()))"
p4 = "(()"
print(parensCheck(p1)) # True
print(parensCheck(p2)) # False
print(parensCheck(p3)) # True
print(parensCheck(p4)) # False
