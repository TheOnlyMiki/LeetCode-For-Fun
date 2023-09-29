# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.output = []
        def dfs(node):
            if node:
                if node.left:
                    dfs(node.left)
                self.output.append(node.val)
                if node.right:
                    dfs(node.right)
        
        dfs(root)
        return self.output
