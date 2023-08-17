import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [-num for num in nums]

        heapq.heapify(nums)

        temp = None
        for x in xrange(k):
            temp = heapq.heappop(nums)

        return -temp
