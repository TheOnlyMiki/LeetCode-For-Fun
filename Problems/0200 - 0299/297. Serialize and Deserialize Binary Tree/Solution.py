# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # Option 2 - DFS method
    """
    def serialize(self, root):
        if not root:
            return ""

        def readTree(nodes, node):
            if node:
                nodes.append(str(node.val))
                readTree(nodes, node.left)
                readTree(nodes, node.right)
            else:
                nodes.append('.')

        store = []
        readTree(store, root)
        return ' '.join(reversed(store))

    def deserialize(self, data):
        def buildTree(nodes):
            if nodes:
                num = nodes.pop()
                if num == '.':
                    return None

                node = TreeNode(int(num))
                node.left = buildTree(nodes)
                node.right = buildTree(nodes)
                return node

            return None
        
        return buildTree(data.split())
        """

    # Option 1 - BFS method
    def serialize(self, root):
        if not root:
            return ""

        nodes = [root]
        output = []
        while nodes:
            next_level = []

            for node in nodes:
                if node:
                    next_level += [node.left, node.right]
                    output.append(str(node.val))
                else:
                    output.append('.')

            nodes = next_level
        
        return ' '.join(reversed(output))

    def deserialize(self, data):
        if not data:
            return None

        data = data.split()
        head = TreeNode(int(data.pop()))
        nodes = [head]

        while nodes:
            next_level = []

            for node in nodes:
                left = data.pop()
                if left != '.':
                    node.left = TreeNode(int(left))
                    next_level.append(node.left)

                right = data.pop()
                if right != '.':
                    node.right = TreeNode(int(right))
                    next_level.append(node.right)
                
            nodes = next_level
        
        return head
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
