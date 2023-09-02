# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Option 2 - Space O(1)
        """
        slow = fast = head
        circle = True
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                circle = False
                break

        if circle:
            return None

        if head == slow:
            return slow
        
        while slow != head:
            slow = slow.next
            head = head.next

        return slow
        """

        # Option 1 - Space O(n)
        record = set()
        while head:
            if head in record:
                return head
                
            record.add(head)
            head = head.next

        return None
