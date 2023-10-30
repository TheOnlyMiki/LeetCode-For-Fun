"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # Option 2 - Queue
        if not head:
            return None

        record = []
        if head.next:
            record.append(head.next)
        if head.child:
            record.append(head.child)
            head.child = None

        prev = head
        while record:
            node = record.pop()

            if node.next:
                record.append(node.next)
            if node.child:
                record.append(node.child)
                node.child = None

            node.prev, prev.next, prev = prev, node, node

        return head

        # Option 1 - DFS
        """
        def dfs(node):
            if node:
                if node.child:
                    temp = node.next
                    node.next, node.child.prev, node.child = node.child, node, None
                    node = dfs(node.next)
                    node.next = temp
                    if temp:
                        temp.prev = node

                return dfs(node.next) if node.next else node

            return

        dfs(head)

        '''
        cur = head
        o = []
        while cur:
            print("current",cur.val)
            if cur.child:
                print("child",cur.child.val)
            if cur.prev:
                print("prev",cur.prev.val)
            if cur.next:
                print("next",cur.next.val)

            print()
            o.append(cur.val)
            cur = cur.next

        print(o)
        '''

        return head
        """
