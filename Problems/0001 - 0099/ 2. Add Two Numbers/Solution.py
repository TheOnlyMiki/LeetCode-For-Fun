# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Option 2 - string operations in python
        """
        head = ListNode()
        record = head

        num = num_2 = ""

        while l1 or l2:
            if l1:
                num += str(l1.val)
                l1 = l1.next
            if l2:
                num_2 += str(l2.val)
                l2 = l2.next

        num = int(num[::-1])
        num_2 = int(num_2[::-1])

        consum = str(num + num_2)[::-1]

        for i in range(len(consum)-1):
            record.val = int(consum[i])
            record.next = ListNode()
            record = record.next

        record.val = int(consum[-1])

        return head
        """

        # Option 1
        head = ListNode()
        record = head
        consum = None
        carry = 0

        while l1 or l2:
            if l1 and l2:
                consum = l1.val + l2.val + carry
                record.next = (ListNode(consum%10) if consum > 9 else ListNode(consum))
                carry = (1 if consum > 9 else 0)
                l1 = l1.next
                l2 = l2.next
            else:
                if l1:
                    consum = l1.val + carry
                    record.next = (ListNode(consum%10) if consum > 9 else ListNode(consum))
                    carry = (1 if consum > 9 else 0)
                    l1 = l1.next
                else:
                    consum = l2.val + carry
                    record.next = (ListNode(consum%10) if consum > 9 else ListNode(consum))
                    carry = (1 if consum > 9 else 0)
                    l2 = l2.next

            record = record.next

        if carry == 1:
            record.next = ListNode(carry)

        return head.next
