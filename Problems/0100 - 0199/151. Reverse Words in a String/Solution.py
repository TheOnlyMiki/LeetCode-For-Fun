class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s = s.split()[::-1]

        """
        output = ""
        for word in s:
            output += word + " "

        return output[:-1]
        """

        return " ".join(s)
