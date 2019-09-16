# linear structure traversal - arrays
fruits = ['apple', 'orange', 'banana']
for fruit in fruits:
   print(fruit)

# linear structure traversal - linked lists

def traverse(self):
   node = self #start from the head node
   while node != None:
      print(node.val)
      node = node.next

# but for trees, you have to it either recursively or iteratively
# or breadth first search / depth first search? I don't get it

# Pre-Order Traversal for DFS - # A B D E C F G
def preTraversal(root):
   if not root:
      return
   print(root.val) # prints the value
   preTraversal(root.left) # recursive, goes all the way down the left side
   preTraversal(root.right) # then the right side when there's no more lefts

#In-Order Traversal - # D B E A F C G
# you can use this for a binary search tree
def inTraversal(root): 
   if not root:
      return
   inTraversal(root.left) # so this goes all the way down the left before printing the first one
   print(root.val)
   inTraversal(root.right)  

#Post-Order Traversal - # D E B F G C A
def inTraversal(root): 
   if not root:
      return
   inTraversal(root.left)
   inTraversal(root.right)  
   print(root.val)
