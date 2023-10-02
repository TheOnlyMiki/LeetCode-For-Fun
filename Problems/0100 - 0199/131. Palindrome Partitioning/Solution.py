class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def checkPalindrome(word):
            if word in record:
                return record[word]

            left, right = 0, len(word)-1
            while left < right:
                if word[left] != word[right]:
                    record[word] = False
                    return False
                left, right = left+1, right-1

            record[word] = True
            return True

        def getOutput(store, word):
            if len(word) == 0:
                output.append(store[:])
                return

            for i in range(1, len(word)+1):
                if checkPalindrome(word[:i]):
                    getOutput(store + [word[:i]], word[i:])
        output = []
        record = {}
        getOutput([], s)
        return output
