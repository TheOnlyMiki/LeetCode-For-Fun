class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        '''
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
        '''

        if len(s) != len(t):
            return False

        # Method 1 - time complexity O(n), space complexity O(s+t)
        count_s, count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1

        return count_s == count_t

        # Method 2 - time complexity O(n logn), space complexity O(1) or O(s+t)
        '''return sorted(s) == sorted(t)
        '''
