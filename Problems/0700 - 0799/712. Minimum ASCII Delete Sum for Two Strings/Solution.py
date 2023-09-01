class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        len1, len2 = len(s1), len(s2)+1
        cols = range(len2-1)
        record1 = [0] * len2
        record2 = c = None

        for i in range(len1):
            record2 = [0] * len2
            c = s1[i]
            for j in cols:
                record2[j] = record1[j-1] + ord(c) if c == s2[j] else max(record2[j-1], record1[j])

            record1 = record2

        return sum(ord(c) for c in s1+s2) - record2[len2-2]*2
