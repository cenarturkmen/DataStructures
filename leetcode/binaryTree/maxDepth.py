#https://leetcode.com/problems/maximum-depth-of-binary-tree/
#o(n) time complexity

def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
    if root is None:
        return 0

    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))