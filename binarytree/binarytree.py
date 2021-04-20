from node import Node

class BinaryTree():
    def __init__(self, root):
        self.root = Node(root)
            
    def print_tree(self,):
        pass

    def preorder(self, root):
        #root >> left >> right
        if root:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)
        

    def inorder(self, root):
        # left >> root >> right
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)

        
    def postorder(self, root):
        # left >> right >> root
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val)

    
    def levelorder(self, root):
        level_order = []
        level = [root]

        while root and level:
            currentNodes = []
            nextLevel = []
            for node in level:
                #print(node.val)
                currentNodes.append(node.val)
                #print("current nodes", currentNodes)
                if node.left:
                    #print(node.val)
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)

            level_order.append(currentNodes)
            level = nextLevel

        return level_order


    def height(self, root):
        if root is None:
            return -1
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        return 1 + max(left_height, right_height)

        
    def size_recursive(self, root):
        if root is None:
            return 0
        return 1 + self.size_recursive(root.left) + self.size_recursive(root.right)


tree = BinaryTree(0)
tree.root.left = Node(1)
tree.root.right = Node(2)
tree.root.left.left = Node(3)
tree.root.left.right = Node(4)
#tree.root.left.left.left = Node(8)

print("preorder traversal")
tree.preorder(tree.root)

print("inorder traversal")
tree.inorder(tree.root)

print("postorder traversal")
tree.postorder(tree.root)

print("levelorder traversal")
print(tree.levelorder(tree.root))

print("height", tree.height(tree.root))

print("size", tree.size_recursive(tree.root))

