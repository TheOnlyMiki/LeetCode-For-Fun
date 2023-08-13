# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class MyNode(object):
    def __init__(self, val, node):
        self.val = val
        self.node = node
    
    def __lt__(self, other):
        return self.val < other.val

    #def __repr__(self):
        #return 'Node value: ' + str(self.val)

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, MyNode(node.val, node))
        
        if not heap:
            return None
        
        head = current = heapq.heappop(heap).node
        if head.next:
            heapq.heappush(heap, MyNode(head.next.val, head.next))

        temp = None
        while heap:
            temp = heapq.heappop(heap).node
            if temp.next:
                heapq.heappush(heap, MyNode(temp.next.val, temp.next))
            current.next = temp
            current = temp

        return head
