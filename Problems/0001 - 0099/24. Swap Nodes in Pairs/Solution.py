# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Option 2
        previou = final_head = ListNode(None, head)
        while head and head.next:
                head.next.next, head, previou.next.next, previou.next, previou = previou.next, head.next.next, head.next.next, head.next, previou.next

        return final_head.next

        # Option 1
        """
        final_head = ListNode(0, head)
        previou, current, even = final_head, head, False
        while current:
            if even:
                previou.next.next, previou.next, previou, current.next, current = current.next, current, previou.next, previou.next, current.next
            else:
                current = current.next
                
            even = not even

        return final_head.next
        """
