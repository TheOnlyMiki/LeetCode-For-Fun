class Solution(object):
    def canBeEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Option 2
        return (
            (s1[0] == s2[0] and s1[2] == s2[2]) or (s1[0] == s2[2] and s1[2] == s2[0])
        ) and (
            (s1[1] == s2[1] and s1[3] == s2[3]) or (s1[1] == s2[3] and s1[3] == s2[1])
        )

        # Option 1
        """
        if s1[0] != s2[0] or s1[2] != s2[2]:
            if s1[0] != s2[2] or s1[2] != s2[0]:
                return False
        if s1[1] != s2[1] or s1[3] != s2[3]:
            if s1[1] != s2[3] or s1[3] != s2[1]:
                return False

        return True
        """
