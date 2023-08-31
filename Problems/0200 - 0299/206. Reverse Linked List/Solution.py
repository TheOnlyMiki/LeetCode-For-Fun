# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Option 2 - Iteration
        previou = temp = None
        current = head
        
        while current:
            temp = current.next
            current.next = previou
            previou = current
            current = temp

        return previou

        # Option 1 - recursively
        """
        def reverseNode(previou, current):
            if current.next:
                temp = current.next
                current.next = previou
                return reverseNode(current, temp)
            else:
                current.next = previou
                return current

        return reverseNode(None, head) if head else None
        """
