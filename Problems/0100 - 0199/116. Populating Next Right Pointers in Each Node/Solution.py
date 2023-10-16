"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        nodes = [root]

        while nodes:
            next_level = []
            pre_node = None

            for node in nodes:
                if pre_node:
                    pre_node.next = node
                pre_node = node

                if node.left:
                    next_level.append(node.left)

                if node.right:
                    next_level.append(node.right)
            
            nodes = next_level

        return root
