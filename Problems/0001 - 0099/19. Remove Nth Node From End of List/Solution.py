# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if head.next is None: 
            return None

        i = 0
        record = ListNode(0, head)
        result_head = record
        delete_node = record

        while i < (n + 1):
            record = record.next
            i += 1

        while record:
            record = record.next
            i += 1
            delete_node = delete_node.next

        delete_node.next = delete_node.next.next

        return result_head.next
