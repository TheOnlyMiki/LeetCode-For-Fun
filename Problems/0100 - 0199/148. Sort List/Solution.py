# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        def merge(left, right):
            if not left:
                return right
            if not right:
                return left

            head, temp, left, right = (left, left, left.next, right) if left.val < right.val else (right, right, left, right.next)
            while left and right:
                if left.val < right.val:
                    temp.next = left
                    left = left.next
                else:
                    temp.next = right
                    right = right.next
                temp = temp.next

            temp.next = left if left else right

            return head

        def mergeSort(node):
            if not node or not node.next: 
                return node

            slow = fast = node
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next

            right = slow.next
            slow.next = None

            return merge(mergeSort(node), mergeSort(right))

        return mergeSort(head)
