# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        values = [root.val]
        nodes = [root]
        next_level = None

        while nodes:
            next_level = []
            for node in nodes:
                if node.left:
                    next_level.append(node.left)
                    values.append(node.left.val)
                if node.right:
                    next_level.append(node.right)
                    values.append(node.right.val)
            nodes = next_level
        
        values = sorted(values)
        output = 1000001
        for i in range(len(values)-1):
            output = min(output, values[i+1] - values[i])

        return output
