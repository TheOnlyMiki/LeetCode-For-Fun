# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def traversal(node):
            if node:
                self.output.append(node.val)
                traversal(node.left)
                traversal(node.right)

        self.output = []
        traversal(root)
        return self.output
