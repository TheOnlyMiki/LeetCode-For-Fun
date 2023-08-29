class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        word_len = set([len(word) for word in wordDict])
        record = { len(s):True }

        def checkValid(start, end):
            if start in record:
                return record[start]

            if s[start:end] in wordDict:
                for n in word_len:
                    if checkValid(end, end+n):
                        return True
                record[end] = False

            return False
        
        for i in word_len:
            if checkValid(0, i):
                return True

        return False
