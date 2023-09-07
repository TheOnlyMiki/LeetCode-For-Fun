class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        len1, len2 = len(text1), len(text2)+1
        cols = range(len2-1)
        record1 = [0] * len2
        record2 = c = None

        for c in text1:
            record2 = [0] * len2
            for j in cols:
                record2[j] = record1[j-1]+1 if c == text2[j] else max(record1[j], record2[j-1])

            record1 = record2

        return record1[len2-2]
