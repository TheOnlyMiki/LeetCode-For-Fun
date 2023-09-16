# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        output, max_i, i = -1e6, 0, 1
        record = [root]

        while record:
            temp = []
            consum = 0
            for node in record:
                consum += node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            
            if consum > output:
                output, max_i = consum, i
            record = temp
            i += 1

        return max_i
