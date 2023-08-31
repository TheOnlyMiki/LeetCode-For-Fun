"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        if not node.neighbors:
            return Node(node.val)

        # Option 1 and 2 almost same speed.

        # Option 2 - adding the neighbors when nodes were traverse
        """
        store = {node:Node(node.val)}
        nodes = [node]
        next_neighbors = None
        while nodes:
            next_neighbors = []
            for n in nodes:
                for n2 in n.neighbors:
                    if n2 not in store:
                        next_neighbors.append(n2)
                        store[n2] = Node(n2.val)
                    store[n].neighbors.append(store[n2])
            nodes = next_neighbors
        """

        # Option 1 - adding the neighbors after all nodes were store
        
        store = {}
        nodes = [node]
        next_neighbors = None
        while nodes:
            next_neighbors = []
            for n in nodes:
                if n not in store:
                    store[n] = Node(n.val)
                for n2 in n.neighbors:
                    if n2 not in store:
                        next_neighbors.append(n2)
                        store[n2] = Node(n2.val)
            nodes = next_neighbors

        for key in store:
            for neighbor in key.neighbors:
                store[key].neighbors.append(store[neighbor])
        

        return store[node]
