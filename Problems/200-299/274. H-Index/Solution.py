class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        #Option 2
        citations.sort()
        h = 0

        #The lowest of the maximum of cites or the maximum of publics
        max_h = min(len(citations), citations[-1])
        for i in range(1, max_h+1):
            if i <= citations[-i]:
                h+=1

        return h
        
        #Option 1
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
        """
