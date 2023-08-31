class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        public = {}
        for i in range(len(s)):
            if s[i] in public:
                if public[s[i]] != t[i]:
                    return False
            elif t[i] in public.values():
                return False
            else:
                public[s[i]] = t[i]

        return True
