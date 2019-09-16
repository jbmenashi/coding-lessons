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


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isSameTree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False

    left = isSameTree(p.left, q.left)
    right = isSameTree(p.right, q.right)

    return left is True and right is True and p.data == q.data


test1 = Node(1)
test1.left = Node(2)
test1.right = Node(3)
test2 = Node(1)
test2.left = Node(2)
test2.right = Node(4)

isSameTree(test1, test2) # false
