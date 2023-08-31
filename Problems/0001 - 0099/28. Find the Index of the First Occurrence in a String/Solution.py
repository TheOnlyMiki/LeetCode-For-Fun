class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        output = -1

        try:
            output = haystack.index(needle)
        except:
            return -1

        return output
