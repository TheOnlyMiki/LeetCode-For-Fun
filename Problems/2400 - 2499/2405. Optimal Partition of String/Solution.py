class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = 1
        #visit = set()
        visit = ""
        for c in s:
            if c in visit:
                output += 1
                #visit = {c}
                visit = c
            else:
                #visit.add(c)
                visit += c

        return output
