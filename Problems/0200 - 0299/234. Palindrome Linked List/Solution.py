# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Option 2 - Space O(1)
        slow = fast = head
        previou = None
        while fast and fast.next:
            fast, slow.next, previou, slow = fast.next.next, previou, slow, slow.next

        if fast:
            slow = slow.next

        while previou and slow:
            if previou.val != slow.val:
                return False
            previou, slow = previou.next, slow.next

        return True

        # Option 1 - Space O(n)
        """
        record = []
        while head:
            record.append(head.val)
            head = head.next

        left, right = 0, len(record)-1
        while left < right:
            if record[left] != record[right]:
                return False
            left += 1
            right -= 1

        return True
        """
