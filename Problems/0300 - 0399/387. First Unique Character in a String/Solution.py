class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = {}
        for i, c in enumerate(s):
            record[c] = -1 if c in record else i

        output = len(s)
        for num in record.values():
            if -1 < num < output:
                output = num
        
        return -1 if output == len(s) else output
