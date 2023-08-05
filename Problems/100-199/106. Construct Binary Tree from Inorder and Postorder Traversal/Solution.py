# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.lastIndex = len(postorder)-1

        def getTree(start, end):
            if start > end:
                return None
            
            node = TreeNode(postorder[self.lastIndex])
            self.lastIndex -= 1

            parent = inorder.index(node.val)

            node.right = getTree(parent+1, end)
            node.left = getTree(start, parent-1)

            return node

        return getTree(0, len(postorder)-1)
