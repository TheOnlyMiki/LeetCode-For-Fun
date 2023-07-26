class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s

        index_0 = numRows + numRows - 2
        count = [ [] for _ in range(numRows) ]
        index_shift = numRows - 2

        for i, c in enumerate(s):
            index = i % index_0
            if index == 0:
                count[0].append(c)
                index_shift = numRows - 2
            elif index < numRows:
                count[index].append(c)
            else:
                count[index_shift].append(c)
                index_shift-=1

        return "".join( [ "".join(count[i]) for i in range(numRows) ] )
