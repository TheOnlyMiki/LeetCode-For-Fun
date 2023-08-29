# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        head = ListNode()
        record = head

        while list1 and list2:
            if list1.val > list2.val:
                record.next = list2
                list2 = list2.next
            else:
                record.next = list1
                list1 = list1.next

            record = record.next

        if list1:
            record.next = list1
        elif list2:
            record.next = list2

        return head.next
