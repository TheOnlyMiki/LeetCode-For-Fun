# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previou = ListNode(-1000)
        current = head
        
        while current:
            if current.val == previou.val:
                previou.next = current.next
            else:
                previou = current

            current = current.next

        return head
