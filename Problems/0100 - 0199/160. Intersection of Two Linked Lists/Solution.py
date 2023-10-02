# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Option 2 - Time O(n+m), Space O(1)
        current_A = headA
        total_A = 0
        while current_A:
            total_A += 1
            current_A = current_A.next

        current_B = headB
        total_B = 0
        while current_B:
            total_B += 1
            current_B = current_B.next

        if total_A > total_B:
            for _ in range(total_A - total_B):
                headA = headA.next
        elif total_A < total_B:
            for _ in range(total_B - total_A):
                headB = headB.next
            total_B = total_A

        for _ in range(total_B):
            if headA == headB:
                return headA
            headA, headB = headA.next, headB.next

        return None

        # Option 1 - Time O(n+m), Space O(n)
        """
        record = set()
        while headA:
            record.add(headA)
            headA = headA.next

        while headB:
            if headB in record:
                return headB
            headB = headB.next

        return None
        """
