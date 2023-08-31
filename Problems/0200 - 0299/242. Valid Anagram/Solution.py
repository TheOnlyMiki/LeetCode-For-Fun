class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s = s.decode()
        t = t.decode()

        count_s = {}
        count_t = {}

        try:
            for i in range(max(len(s), len(t))):
                if s[i] in count_s:
                    count_s[s[i]] += 1
                else:
                    count_s[s[i]] = 1

                if t[i] in count_t:
                    count_t[t[i]] += 1
                else:
                    count_t[t[i]] = 1
        except:
            return False

        return count_s == count_t
