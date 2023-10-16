# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                self.output.append(node.val)

        self.output = []
        dfs(root)
        return self.output
