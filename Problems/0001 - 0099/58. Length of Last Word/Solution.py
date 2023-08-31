class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Option 2
        consum = 0

        for i in s[::-1]:
            if i != ' ':
                consum+= 1
            elif consum != 0:
                return consum

        #Option 1
        return len(s.split()[-1])
