# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        record = {0:1}
        self.output = 0

        def dfs(node, total):
            if node:
                total += node.val

                if total - targetSum in record:
                    self.output += record[total - targetSum]

                if total in record:
                    record[total] += 1
                else:
                    record[total] = 1

                dfs(node.left, total)
                dfs(node.right, total)

                record[total] -= 1

        dfs(root, 0)
        return self.output
