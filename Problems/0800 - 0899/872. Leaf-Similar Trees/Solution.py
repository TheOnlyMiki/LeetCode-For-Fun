# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        left, right = [], []
        def dfsLeft(node):
            leaf = True
            if node.left:
                leaf = False
                dfsLeft(node.left)
            if node.right:
                leaf = False
                dfsLeft(node.right)
            if leaf:
                left.append(node.val)

        def dfsRight(node):
            leaf = True
            if node.left:
                leaf = False
                dfsRight(node.left)
            if node.right:
                leaf = False
                dfsRight(node.right)
            if leaf:
                right.append(node.val)

        dfsLeft(root1)
        dfsRight(root2)

        return left == right
