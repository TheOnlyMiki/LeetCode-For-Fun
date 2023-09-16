# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, maximum):
            if node:
                if node.val < maximum:
                    return dfs(node.left, maximum) + dfs(node.right, maximum)

                return dfs(node.left, node.val) + dfs(node.right, node.val) + 1
                
            return 0

        return dfs(root, root.val)
