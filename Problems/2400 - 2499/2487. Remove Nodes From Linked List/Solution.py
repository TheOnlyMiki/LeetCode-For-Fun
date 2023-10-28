# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Option 2
        stack = [ListNode(1e6)]
        while head:
            while stack[-1].val < head.val:
                stack.pop()

            stack[-1].next = head
            stack.append(head)
            head = head.next

        return stack[1]

        # Option 1
        """
        stack = []
        while head:
            while stack and stack[-1].val < head.val:
                stack.pop()

            if stack: stack[-1].next = head
                
            stack.append(head)
            head = head.next

        '''
        i = 1
        while i < len(stack):
            stack[i-1].next, i = stack[i], i+1
            '''

        return stack[0]
        """
