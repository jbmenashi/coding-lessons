class Solution(object):
   def maxDepth(self, root):
      if not root:
         return 0 # so if there's no root at all, return 0
      left = self.maxDepth(root.left) # goes down the left side until it you return zero
      right = self.maxDepth(root.right) # same here
      return max(left, right) + 1 # and once you get here, you're returning 1
