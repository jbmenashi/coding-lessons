# determine if a tree is height balanced
# in which the depth of the two subtrees never differs by more than 1

    3
   / \
  9  20
    /  \
   15   7

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
def getHeight(r):
    if not r: return 0
    left = getHeight(r.left)
    right = getHeight(r.right)
    if abs(left - right) > 1: 
        r.isBalanced = False
    return max(left, right) + 1

def isBalanced(r):
    r.isBalanced = True
    getHeight(r)
    return r.isBalanced

root = Node(3) 
root.left = Node(9) 
root.right = Node(20) 
root.right.left = Node(15) 
root.right.right = Node(7) 

if isBalanced(root): 
    print("Tree is balanced") 
else: 
    print("Tree is not balanced") 
