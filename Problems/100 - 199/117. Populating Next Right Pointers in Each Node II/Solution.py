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
        next_level = None
        pre_node = None

        while nodes:
            next_level = []
            pre_node = None

            for node in nodes:
                if node.left:
                    next_level.append(node.left)
                    # Option 2 - Do it in place
                    if pre_node:
                        pre_node.next = node.left
                    pre_node = node.left

                if node.right:
                    next_level.append(node.right)
                    # Option 2 - Do it in place
                    if pre_node:
                        pre_node.next = node.right
                    pre_node = node.right

            # Option 1 - after storing
            """
            for i in range(len(next_level) - 1):
                next_level[i].next = next_level[i + 1]
            """
            
            nodes = next_level

        return root
