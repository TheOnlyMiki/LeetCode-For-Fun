# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def checkSame(p, q):
            if p and q:
                if p.val == q.val:
                    return checkSame(p.left, q.left) and checkSame(p.right, q.right)
                else:
                    return False
            elif p:
                return False
            elif q:
                return False
            return True

        # Option 1
        """
        def checkSame(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            elif p.val != q.val:
                return False
            return checkSame(p.left, q.left) and checkSame(p.right, q.right)
        """

        return checkSame(p, q)
