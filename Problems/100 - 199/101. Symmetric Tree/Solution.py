# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def checkSymmetric(left, right):
            if left and right:
                if left.val == right.val:
                    return checkSymmetric(left.left, right.right) and checkSymmetric(left.right, right.left)
                else:
                    return False
            elif left:
                return False
            elif right:
                return False
            return True
            
        # Option 1
        """
        def checkSymmetric(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False
            return checkSymmetric(left.left, right.right) and checkSymmetric(left.right, right.left)
            """

        return checkSymmetric(root.left, root.right)
