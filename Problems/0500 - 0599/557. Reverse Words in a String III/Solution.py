class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s[::-1].split()[::-1])
        #return ' '.join(word[::-1] for word in s.split())
