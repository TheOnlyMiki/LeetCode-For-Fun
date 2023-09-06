class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        target = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left, right = 0, len(s)-1

        while left < right:
            while left < right and s[left] not in target:
                left += 1

            while left < right and s[right] not in target:
                right -= 1

            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)
