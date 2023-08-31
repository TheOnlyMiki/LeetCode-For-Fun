class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs = sorted(pairs, key=(lambda x:x[1]))

        output, b = 1, pairs[0][1]
        for c, d in pairs:
            if b < c:
                output += 1
                b = d

        return output
