# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        return_head = previou = ListNode(next=head)
        while head:
            if head.val == val:
                previou.next = head.next
            else:
                previou = head
            head = head.next

        return return_head.next
