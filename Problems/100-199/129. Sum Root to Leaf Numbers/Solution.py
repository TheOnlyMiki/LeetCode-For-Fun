# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def findNumber(root):
            if root.left and root.right:
                count = []
                c = str(root.val)
                count.extend(findNumber(root.left))
                count.extend(findNumber(root.right))
                return [ c + number for number in count ]
            elif root.left:
                count = []
                c = str(root.val)
                count.extend(findNumber(root.left))
                return [ c + number for number in count ]
            elif root.right:
                count = []
                c = str(root.val)
                count.extend(findNumber(root.right))
                return [ c + number for number in count ]
            else:
                return str(root.val)

        return sum([ int(n) for n in findNumber(root) ])
