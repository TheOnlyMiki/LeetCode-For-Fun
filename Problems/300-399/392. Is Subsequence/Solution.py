class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        record = 0
        n = len(t)

        try:
            for c in s:
                record += t[record:].index(c) + 1
                if record > n:
                    return False
        except:
            return False

        return True
