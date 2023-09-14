# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        even = head
        odd = odd_head = head.next if even else None
        current = head.next.next if odd else None
        i = True

        while current:
            if i:
                even.next = current
                even = current
                i = False
            else:
                odd.next = current
                odd = current
                i = True

            current = current.next

        if even and odd_head:
            even.next = odd_head
            odd.next = None

        return head
