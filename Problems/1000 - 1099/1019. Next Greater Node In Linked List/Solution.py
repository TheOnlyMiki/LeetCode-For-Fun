# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        # Option 2 - Traversal only one time for linked list
        """
        output, stack = [], []
        while head:
            while stack and stack[-1][0] < head.val:
                output[stack.pop()[1]] = head.val
            
            stack.append([head.val, len(output)])
            output.append(0)
            head = head.next

        return output
        """

        # Option 1 - Reverse the linked list then traversal, this saves a lot of memory spaces
        previou, i = None, 0
        while head:
            head.next, head, previou, i = previou, head.next, head, i+1

        output, stack, i = [0]*i, [], i-1
        while previou:
            while stack and stack[-1] <= previou.val:
                stack.pop()

            if stack:
                output[i] = stack[-1]

            stack.append(previou.val)
            i, previou = i-1, previou.next
        
        return output
