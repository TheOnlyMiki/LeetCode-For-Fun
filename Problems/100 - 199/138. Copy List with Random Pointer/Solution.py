"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # Option 2 - Use map(hash table) instead list
        nodes = {None:None}
        record = head

        while record:
            nodes[record] = Node(record.val)
            record = record.next

        record = head
        while record:
            nodes[record].next = nodes[record.next]
            nodes[record].random = nodes[record.random]
            record = record.next

        return nodes[head]

        # Option 1 - Use list to store head infos , it was Slow
        """
        # nodes[0] ==> original, nodes[1] ==> copy
        nodes = [[], []]

        length = 0
        record = head
        while record:
            nodes[0].append(record)
            nodes[1].append(Node(record.val))
            record = record.next
            length += 1

        for i in range(length):
            nodes[1][i].next = (None if i+1 == length else nodes[1][i+1])
            if nodes[0][i].random in nodes[0]:
                record = nodes[0].index(nodes[0][i].random)
                nodes[1][i].random = nodes[1][record]
            
        return (nodes[1][0] if length > 0 else None)
        """
