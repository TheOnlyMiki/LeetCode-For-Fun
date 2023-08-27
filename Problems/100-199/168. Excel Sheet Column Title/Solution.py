class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        output = ""
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        num, remain = columnNumber, None

        while num > 0:
            num, remain = divmod(num-1, 26)
            output = s[remain] + output

        return output
