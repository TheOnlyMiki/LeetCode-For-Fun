# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        visit = set()
        record = {}

        def dfs(node):
            if node:
                nodename = str(node.val) + ',' + dfs(node.left) + ',' + dfs(node.right)
                if nodename in visit:
                    record[nodename] = node

                visit.add(nodename)
                return nodename

            return 'n'

        dfs(root.left)
        dfs(root.right)
        
        return [ node for node in record.values() ]
