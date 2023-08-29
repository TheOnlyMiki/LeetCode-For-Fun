class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length < 2:
            return s

        def checkPalindrome(left, right):
            while left > -1 and right < length and s[left] == s[right]:
                left -= 1
                right += 1

            return (left+1, right)

        record = (None, None)
        record_length = temp1 = temp2 = 0

        for i in range(length):
            temp1 = checkPalindrome(i, i)
            temp2 = checkPalindrome(i, i+1)
            
            temp1 = (temp2, temp2[1] - temp2[0]) if temp2[1] - temp2[0] > temp1[1] - temp1[0] else (temp1, temp1[1] - temp1[0])
            if temp1[1] > record_length:
                record_length = temp1[1]
                record = temp1[0]
        
        return s[record[0] : record[1]]
