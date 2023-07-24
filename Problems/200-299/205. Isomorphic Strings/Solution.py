class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        public_s = {}
        public_t = {}
        for i in range(len(s)):
            if public_s.get(s[i]) != public_t.get(t[i]):
                return False
            public_s[s[i]] = i
            public_t[t[i]] = i

        return True
