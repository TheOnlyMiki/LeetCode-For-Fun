class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #Option 2
        i = 0

        try:
            for c in t:
                if s[i] == c:
                    i+=1
        except:
            return True
        
        return i == len(s)

        #Option 1
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
        """

        return True
