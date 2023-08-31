# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None

        record_list = []

        record = head
        i = 0
        
        while record:
            record_list.append(record)
            record = record.next
            i += 1

        shift = k % i
        record = head

        if shift != 0:
            record_list[-1].next = head
            record_list[i - shift - 1].next = None
            return record_list[i - shift]
        else:
            return head
