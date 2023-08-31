# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        output = [[root.val]]
        nodes = [root]
        next_level = store = None
        direction = -1

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
                output.append(store[::direction])
                direction = (-1 if direction == 1 else 1)
                """
                # Let direction = boolean
                if direction:
                    output.append(store)
                    direction = False
                else:
                    output.append(store[::-1])
                    direction = True
                """

        return output
