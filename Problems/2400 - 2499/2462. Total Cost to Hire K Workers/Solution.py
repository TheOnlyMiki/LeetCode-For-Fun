import heapq
class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        left, right = 0, len(costs)-1
        output = 0
        first, last = [], []
        while left < candidates and left <= right:
            heapq.heappush(first, costs[left])
            left += 1
        
        while len(last) < candidates and left <= right:
            heapq.heappush(last, costs[right])
            right -= 1

        while k != 0 and left <= right:
            k -= 1
            if first[0] > last[0]:
                output += heapq.heappop(last)
                heapq.heappush(last, costs[right])
                right -= 1
            else:
                output += heapq.heappop(first)
                heapq.heappush(first, costs[left])
                left += 1

        if k != 0:
            output += sum(sorted(first + last)[:k])

        return output
