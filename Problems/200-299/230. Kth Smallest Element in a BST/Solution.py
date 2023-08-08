# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # Option 2 - Use stack, BST means left node always smaller than the parent, and right node is larger than itself's parent, but not larger than other parents of itself's parent
        self.stack = []

        def pushStack(root):
            while root:
                self.stack.append(root)
                root = root.left
        
        pushStack(root)

        temp = None
        for i in range(k):
            temp = self.stack[-1]
            self.stack.pop()
            pushStack(temp.right)

        return temp.val

        # Option 1 - BFS then sorted the whole value of nodes, then find the k index in list
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

        return sorted(values)[k-1]
        """
