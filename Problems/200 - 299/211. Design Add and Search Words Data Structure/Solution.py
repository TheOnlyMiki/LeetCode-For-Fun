class WordDictionary(object):

    def __init__(self):
        self.words = set()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.words.add(word)
        for i in xrange(len(word)):
            self.words.add(word[:i]+'.'+word[i+1:])

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word in self.words:
            return True
        else:
            if word.count('.') == 0:
                return False
            else: 
                i = word.index('.')
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if word[:i] + c + word[i+1:] in self.words:
                        return True
        
        return False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
