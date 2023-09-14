# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        output = 0
        slow = fast = head
        previou = None

        while fast and fast.next:
            fast, slow.next, slow, previou = fast.next.next, previou, slow.next, slow

        while slow and previou:
            if slow.val + previou.val > output:
                output = slow.val + previou.val
            slow, previou = slow.next, previou.next

        return output
