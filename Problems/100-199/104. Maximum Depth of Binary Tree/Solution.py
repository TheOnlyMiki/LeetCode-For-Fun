# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getDepth(root):
            if root:
                return max(getDepth(root.left), getDepth(root.right)) + 1
            else:
                return 0

        return getDepth(root)
