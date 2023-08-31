class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0

        output = 1
        i = 1
        record = s[0]

        for c in s:
            if c in record:
                record = record[record.index(c) + 1:] + c
            else:
                record += c
                output = max(output, len(record))

        return output
