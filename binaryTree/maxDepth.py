class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maxDepth(root):
      if not root:
         return 0 # so if there's no root at all, return 0
      left = maxDepth(root.left) # goes down the left side until it you return zero
      right = maxDepth(root.right) # same here
      return max(left, right) + 1 # and once you get here, you're returning 1


test = Node(3)
test.left = Node(9)
test.right = Node(20)
test.right.left = Node(15)
test.right.right = Node(7)

maxDepth(test)