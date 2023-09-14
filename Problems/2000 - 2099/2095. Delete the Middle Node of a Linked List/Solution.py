# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = fast = head
        previou = None
        while fast and fast.next:
            fast = fast.next.next
            previou = slow
            slow = slow.next

        if previou:
            previou.next = slow.next
            return head
        
        return None
