'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

       1
      / \
   /       \
  2         2
 / \       / \
3   4     4   3

n1.left n2.right
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
 / \   \
3   3    3
'''

# Base Case:
# if node1 and node2 are both null, return true; otherwise if one of them is null return false

# Recursive rule
# Request:
# 1. is node1's left equal to node2's right
# 2. is node1's right equal to node2's left

# Result:
# true if both request 1 and request 2 are true
# we still need to define what "like" means in our recursive rule...


class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
    	if not root.left and not root.right:
    	    return True
    	return self.areEqual(root.left, root.right)

    def areEqual(self, node1, node2):
        # Code here
