class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        n = len(s)

        s = s.lower()
        for c in s:
            if 96 < ord(c) < 123 or 47 < ord(c) < 58:
                s += c

        s = s[n:]
        
        return s == s[::-1]
