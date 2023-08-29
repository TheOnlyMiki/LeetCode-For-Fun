import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        consum = w
        valid = []
        invalid = []

        for p, c in zip(profits, capital):
            if c > w:
                heapq.heappush(invalid, (c, p))
            else:
                heapq.heappush(valid, -p)

        while k != 0 and valid:
            consum += -heapq.heappop(valid)

            while invalid and consum >= invalid[0][0]:
                heapq.heappush(valid, -heapq.heappop(invalid)[1])
            
            k -= 1

        return consum
