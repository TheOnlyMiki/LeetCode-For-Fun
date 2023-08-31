class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        words = [beginWord]
        length = range(len(endWord))
        transform = 1
        next_words = None
        maps = {}
        for word in wordList:
            for i in length:
                word2 = word[:i] + ' ' + word[i+1:]
                if word2 in maps:
                    maps[word2].append(word)
                else:
                    maps[word2] = [word]

        visit = set()
        temp = None
        
        while words:
            next_words = []
            for word in words:
                if word == endWord:
                    return transform

                if word not in visit:
                    visit.add(word)

                    for i in length:
                        temp = word[:i] + ' ' + word[i+1:]
                        if temp in maps:
                            next_words.extend(maps[temp])
                            del maps[temp]

            words = next_words
            transform += 1

        return 0

        # Option 1
        """
        words = [beginWord]
        transform = 1
        next_words = None
        start = end = temp = None
        wordList = set(wordList)
        endCase = {endWord}
        length = range(len(endWord))

        while words:
            next_words = []
            for word in words:
                if word in endCase:
                    return transform
                
                for i in length:
                    start, end = word[:i], word[i+1:]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        temp = start + c + end
                        if temp in wordList:
                            next_words.append(temp)
                            wordList.remove(temp)

            words = next_words
            transform += 1

        return 0
        """
