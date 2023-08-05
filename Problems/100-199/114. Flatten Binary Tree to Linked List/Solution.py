# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        def makeFlatten(root):
            if root.left and root.right:
                #print("left and right:", root.val)
                node = makeFlatten(root.left)
                node2 = makeFlatten(root.right)
                #print("node:", node.val,"node2:",node2.val)
                node.right = root.right
                root.right = root.left
                root.left = None
                return node2
            elif root.left:
                root.right = root.left
                root.left = None
                return makeFlatten(root.right)
            elif root.right:
                #print("right:", root.val)
                return makeFlatten(root.right)
            else:
                #print("else:", root.val)
                return root

        makeFlatten(root)
