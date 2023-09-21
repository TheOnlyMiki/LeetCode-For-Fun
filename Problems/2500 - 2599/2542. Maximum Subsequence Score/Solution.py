import heapq
class Solution(object):
    def maxScore(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        record = []
        total = 0
        output = 0

        for num2, num1 in sorted(zip(nums2, nums1), reverse=True):
            heapq.heappush(record, num1)
            total += num1
            if len(record) == k:
                output = max(output, total * num2)
                total -= heapq.heappop(record)

        return output
