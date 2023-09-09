# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getDepth(node):
            if node:
                left, record1 = getDepth(node.left)
                right, record2 = getDepth(node.right)
                return max(left, right) + 1, max(left + right, record1, record2)

            return 0, 0

        return getDepth(root)[1]
