# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        start = TreeNode(None, root)
        previou, node = start, root
        while node:
            if node.val == key:
                break
            
            previou, node = node, node.left if node.val > key else node.right

        if node:
            fromLeft = (previou.left and previou.left.val == node.val)
            current = None
            if node.left:
                parent, current = node, node.left
                while current.right:
                    parent, current = current, current.right

                current.right, parent.right = node.right, None
                if node.left.val == current.val:
                    node.left = None

                parent = current
                while parent.left:
                    parent = parent.left

                parent.left = node.left
                
            elif node.right:
                parent, current = node, node.right
                while current.left:
                    parent, current = current, current.left

                current.left, parent.left = node.left, None
                if node.right.val == current.val:
                    node.right = None

                parent = current
                while parent.right:
                    parent = parent.right

                parent.right = node.right

            if fromLeft:
                previou.left = current
            else:
                previou.right = current

        return start.left
