import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Option 2 - Heap in k size
        record = nums[:k]
        heapq.heapify(record)

        for i in xrange(k, len(nums)):
            if nums[i] > record[0]:
                heapq.heappushpop(record, nums[i])
        
        return record[0]

        # Option 1 - Heap whole list
        nums = [-num for num in nums]

        heapq.heapify(nums)

        temp = None
        for x in xrange(k):
            temp = heapq.heappop(nums)

        return -temp
