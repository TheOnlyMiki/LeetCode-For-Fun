# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def getNumbers(root):
            level = 0
            left_node = right_node = root
            right_level = 0
            while left_node:
                left_node = left_node.left
                level += 1
                if right_node:
                    right_node = right_node.right
                    right_level = level

            if right_level == level:
                return 2**level - 1
            return getNumbers(root.left) + 1 + getNumbers(root.right)

        return getNumbers(root)

        # Option 1 - O(n), no idea why it was beats 95%, it should be slowly cause O(n)
        """
        def getNumbers(root):
            if not root:
                return 0

            return getNumbers(root.left) + 1 + getNumbers(root.right)

        return getNumbers(root)
        """
