# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        node_small = ListNode()
        node_great = ListNode()
        head_small = node_small
        head_great = node_great
        record = head

        while record:
            if record.val < x:
                node_small.next = record
                node_small = node_small.next
            else:
                node_great.next = record
                node_great = node_great.next
            record = record.next

        node_small.next = node_great.next = None
        node_small.next = head_great.next

        return head_small.next
