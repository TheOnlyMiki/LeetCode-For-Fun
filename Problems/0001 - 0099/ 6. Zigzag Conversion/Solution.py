class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        #Option 2
        count = [ "" for _ in range(numRows) ]
        index_shift = 1
        i = 0
        index_return = numRows-1

        for c in s:
            count[i] += c
            if i == 0:
                index_shift = 1
            elif i == index_return:
                index_shift = -1
            i+=index_shift

        return "".join(count)

        #Option 1
        """
        index_0 = numRows + numRows - 2
        count = [ "" for _ in range(numRows) ]
        index_shift = 0

        for i, c in enumerate(s):
            index = i % index_0
            if index == 0:
                count[0] += c
                index_shift = numRows - 2
            elif index < numRows:
                count[index] += c
            else:
                count[index_shift] += c
                index_shift-=1

        return "".join(count)
        """
