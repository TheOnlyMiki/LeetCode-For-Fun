class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        public = {'s':{}, 't': {}}
        for i in range(len(s)):
            if public['s'].get(s[i]) != public['t'].get(t[i]):
                return False
            public['s'][s[i]] = i
            public['t'][t[i]] = i

        return True
