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


