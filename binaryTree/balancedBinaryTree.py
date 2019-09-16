# determine if a tree is height balanced
# in which the depth of the two subtrees never differs by more than 1

    3
   / \
  9  20
    /  \
   15   7

class Solution(object):
   def isBalanced(self, root):
      self.isBalanced = True
      self.getHeight(root)
      return self.isBalanced

   def getHeight(self, root):
      if not root:
         return 0
      left = self.getHeight(root.left)
      right = self.getHeight(root.right)
      if abs(left - right) > 1:
         self.isBalanced = False
      return max(left, right) + 1
