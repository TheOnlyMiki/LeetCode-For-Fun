# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def checkDepth(node):
            if node:
                left_depth = checkDepth(node.left)
                if left_depth == -1:
                    return -1
                right_depth = checkDepth(node.right)
                if right_depth == -1:
                    return -1
                if abs(left_depth - right_depth) > 1:
                    return -1

                return max(left_depth, right_depth) + 1
            
            return 0

        return checkDepth(root) != -1
