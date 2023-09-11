class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = {'a','e','i','o','u'}
        count = sum( 1 if s[i] in vowels else 0 for i in range(k) )
        maximum = count

        for i in range(k, len(s)):
            if s[i-k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1

            if count > maximum:
                maximum = count

        return maximum
