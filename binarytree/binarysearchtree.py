from node import Node

class BinarySearchTree():
    def __init__(self, root):
        self.root = Node(root)

    def search(self, root, val):
        if val == self.root:
            return True
        elif val < self.root:
            return self.search(root.left, val)
        
        return self.search(root.right, val)
        
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, current_node, val):
        if val < current_node.val:
            if current_node.left is None:
                current_node.left = Node(val)
            else:
                self._insert(current_node.left, val)
        elif val > current_node.val:
            if current_node.right is None:
                current_node.right = Node(val)
            else:
                self._insert(current_node.right, val)
        else:
            print("this val is already exist")

    def preorder(self, root):
        if root:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

bst = BinarySearchTree(4)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(14)
bst.preorder(bst.root)
"""
            4
       3         10
    1  None  None  14
"""


"""
tree = BinarySearchTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)
tree.preorder(tree.root)


                    1
            2               3
        4      5        6       7
                                    8

"""