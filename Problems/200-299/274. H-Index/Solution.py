class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        n = len(citations)
        count = { i:0 for i in range(n+1) }

        for value in citations:
            if value in count:
                count[value] += 1
            else:
                count[n] += 1

        for i in range(n, 0, -1):
            if count[i] >= i:
                return i
            else:
                count[i-1] += count[i]

        return 0
