# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None:
            return None

        previous = ListNode()
        result_head = previous
        check_node = head
        record = head.next
        last_node_check = True

        while record:
            if record.val != check_node.val:
                previous.next = check_node
                previous = previous.next
                previous.next = None
                check_node = record
            else:
                while record.next and record.next.val == check_node.val:
                    record = record.next

                if record.next == None:
                    last_node_check = False
                    break

                record = record.next
                check_node = record
            
            record = record.next

        if last_node_check:
            previous.next = check_node

        return result_head.next
