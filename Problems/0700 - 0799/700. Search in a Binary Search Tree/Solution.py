# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # Option 2
        while root:
            if root.val == val:
                return root
            
            root = root.left if root.val > val else root.right

        return None

        # Option 1
        """
        def dfs(node):
            if node:
                if node.val > val:
                    return dfs(node.left)
                elif node.val < val:
                    return dfs(node.right)
                else:
                    return node

            return None

        return dfs(root)
        """
