# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def doubleIt(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Option 2
        current = previou = head
        if head.val > 4:
            head = previou = ListNode(0, head)
        
        represent = {1:2, 2:4, 3:6, 4:8, 5:0, 6:2, 7:4, 8:6, 9:8, 0:0}
        while current:
            if current.val > 4:
                previou.val += 1
            
            current.val = represent[current.val]
            previou, current = current, current.next

        return head
        
        # Option 1
        """
        current = previou = head
        if head.val > 4:
            head = previou = ListNode(0, head)

        temp = None
        while current:
            temp = current.val * 2
            if temp > 9:
                previou.val += 1
                current.val = temp - 10
            else:
                current.val = temp

            previou, current = current, current.next

        return head
        """
