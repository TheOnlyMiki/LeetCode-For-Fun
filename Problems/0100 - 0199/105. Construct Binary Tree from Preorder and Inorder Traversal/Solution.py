# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def getTree(preorder, inorder, length):
            root = inorder.index(preorder[0])
            node = TreeNode(preorder[0])
            if root != 0:
                node.left = getTree(preorder[1:length], inorder, root)
            if root != length - 1:
                node.right = getTree(preorder[root+1:length], inorder[root+1:length], length - root - 1)
            return node

        return getTree(preorder, inorder, len(preorder))
