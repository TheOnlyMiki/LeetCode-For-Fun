# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        def findSum(root, consum):
            next_consum = consum + root.val
            if root.left and root.right:
                #print("left and right:", consum + root.val)
                return findSum(root.left, next_consum) or findSum(root.right, next_consum)
            elif root.left:
                #print("left:", consum + root.val)
                return findSum(root.left, next_consum)
            elif root.right:
                #print("right:", consum + root.val)
                return findSum(root.right, next_consum)
            else:
                #print("else:", consum + root.val)
                return next_consum == targetSum

        return findSum(root, 0)
