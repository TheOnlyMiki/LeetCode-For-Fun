class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        min_len = min(len(word1), len(word2))
        output = ""
        i = 0
        even = True

        while i < min_len:
            if even:
                output += word1[i]
            else:
                output += word2[i]
                i += 1
            
            even = not even

        output += word1[i:]
        output += word2[i:]

        return output
