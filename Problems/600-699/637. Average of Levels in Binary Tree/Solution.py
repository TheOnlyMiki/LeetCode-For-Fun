# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []

        output = [float(root.val)]
        nodes = [root]
        next_level = store = None

        while nodes:
            next_level = []
            store = []
            for node in nodes:
                if node.left:
                    next_level.append(node.left)
                    store.append(node.left.val)
                if node.right:
                    next_level.append(node.right)
                    store.append(node.right.val)
            nodes = next_level
            if store:
                output.append(float(sum(store)) / len(store))

        return output
