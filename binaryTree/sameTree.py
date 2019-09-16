'''
Given two binary trees, write a function to check if they are the same or not.
Example 1:

         tree 1    tree 2
Input:     1         1
          / \       / \
         2   3     2   3
         
         root1      root2
Output: true
Example 2:
Input:     1         1
          /           \
         2             2
Output: false
Example 3:
Input:     1         1
          / \       / \
         2   1     1   2
Output: false
'''
# Base Case:
#   When either of node == None, compare it to the other node.
# Recursive rule
# Request:
# 1. are both node's left subtree the same or not?
# 2. are both node's right subtree the same or not?
# Result:
# if the left and right subtrees are identical AND the values of the current node are the same, return True, if not return False


class Solution(object):
    def isSameTree(self, p, q):
        # Base Case
        if not p and not q:
            return True
        '''
        0 0 => true
        0 1 => false
        1 0 => false
        '''
        # Base Case
        # p or q
        if not p or not q:
            return False

        # OR:
           # if not p and q: return False
           # if not q and p: return False

        # Request
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        # Return
        return left is True and right is True and p.val == q.val
