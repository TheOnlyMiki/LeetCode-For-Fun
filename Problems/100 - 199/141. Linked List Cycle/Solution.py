# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Option 2
        fast_node = head

        while fast_node and fast_node.next:
            if fast_node.next == head:
                return True
            head = head.next
            fast_node = fast_node.next.next

        return False

        # Option 1 - Misunderstand the question, the whole node is indetify as 
        # val and next, if there are two nodes has same val, but different next, 
        # then this two nodes are inconsistent.
        """
        if head == None:
            return False

        nodes = set()
        next_node = head.next
        nodes.add(head.val)

        try:
            while next_node != None:
                if next_node in nodes:
                    return True
                
                nodes.add(next_node)
                next_node = next_node.next
        except:
            return False

        return False
        """
