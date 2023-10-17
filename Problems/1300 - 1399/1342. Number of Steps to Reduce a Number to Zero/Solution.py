class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        output = 0
        while num != 0:
            output += 1
            if num & 1 == 1:
                num -= 1
            else:
                num /= 2

        return output
