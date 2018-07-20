from collections import deque

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    stack = deque()
    stack.append(self)
    while (len(stack) > 0):
      x = stack.pop()
      print(x.value)
      cb(x.value)
      if (x.right != None):
        stack.append(x.right)
      if (x.left != None):
        stack.append(x.left)

  def breadth_first_for_each(self, cb):
    queue = deque([])
    queue.append(self)
    while (len(queue) > 0):
      x = queue.popleft()
      print(x.value)
      cb(x.value)
      if (x.left != None):
        queue.append(x.left)
      if (x.right != None):
        queue.append(x.right)

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
