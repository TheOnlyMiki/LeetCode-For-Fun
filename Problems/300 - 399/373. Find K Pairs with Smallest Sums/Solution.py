import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        temp = None
        record = []
        for x in nums1:
            for y in nums2:
                temp = -(x + y)
                if len(record) < k:
                    heapq.heappush(record, (temp, x, y))
                elif temp > record[0][0]:
                    heapq.heappushpop(record, (temp, x, y))
                else:
                    break

        return [[x, y] for _, x, y in record]
