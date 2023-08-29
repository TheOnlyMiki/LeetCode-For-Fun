class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        count_p = {}
        count_s = {}

        s = s.split()
        if len(s) != len(pattern):
            return False

        try:
            for i, word in enumerate(s):
                if pattern[i] in count_p or word in count_s:
                    if count_p[pattern[i]] != word or count_s[word] != pattern[i]:
                        return False
                else:
                    count_p[pattern[i]] = word
                    count_s[word] = pattern[i]
        except:
            return False

        return True
