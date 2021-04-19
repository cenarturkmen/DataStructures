class Node():
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def inorder(temp):
    if (not temp):
        return
 
    inorder(temp.left)
    print(temp.val,end = " ")
    inorder(temp.right)

root = Node(0)
"""
        0
      /   \
     None  None
"""

root.left = Node(1)
root.right = Node(2)

"""
           0
         /     \
        1       2
     /    \    /  \
   None None None None"""

root.left.left = Node(34)

'''
           0
       /       \
      1          2
    /   \       /  \
   34    None  None  None
  /  \
None None'''

#maximum number of nodes at level "l" of a binary tree is 2^l
#maximum number of nodes in a binary tree of height ‘h’ is 2^h – 1 
print("Inorder traversal before insertion:", end = " ")
inorder(root)