# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseOperation(self, record, end):
        start = record.next
        record.next = end
        return start, record

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 1 -> 2 -> 3, let's say we at 2
        # start for recording the address of 3
        # end for recording the address 2 itself
        start = None
        end = None
        i = 0
        record = head
        
        # Find a head for result, and why not just reversing during this period?
        while record and i < k:
            record, end = self.reverseOperation(record, end)
            i += 1

        node_may_reverse_back = end
        result_head = end
        connect_node = None
        output_head = head
        
        while record:
            i = 0
            connect_node = record
            end = None

            while record and i < k:
                record, end = self.reverseOperation(record, end)
                i += 1

            node_may_reverse_back = output_head
            output_head.next = end
            output_head = connect_node

        if 1 < i < k:
            record = end
            start = end = None
            while record and i > 0:
                record, end = self.reverseOperation(record, end)
                i -= 1
            node_may_reverse_back.next = end

        return result_head
