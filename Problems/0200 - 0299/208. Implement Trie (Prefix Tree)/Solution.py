class Trie(object):
    def __init__(self):
        self.elements = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        temp = self.elements
        for c in word:
            if c in temp:
                temp = temp[c]
            else:
                temp[c] = {}
                temp = temp[c]

        temp[True] = None

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        temp = self.elements
        for c in word:
            if c in temp:
                temp = temp[c]
            else:
                return False

        return True in temp

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        temp = self.elements
        for c in prefix:
            if c in temp:
                temp = temp[c]
            else:
                return False

        return True
# Option 1 - too complicated
'''
class MyNode(object):
        def __init__(self, val='', next={}):
            self.val = val
            self.next = next

class Trie(object):
    def __init__(self):
        self.elements = {}
        self.items = set()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        if word not in self.items:
            self.items.add(word)

        temp = None
        if word[0] in self.elements:
            node = self.elements[word[0]]
            for i in xrange(1, len(word)):
                if word[i] in node.next:
                    node = node.next[word[i]]
                else:
                    temp = MyNode(word[i], {})
                    node.next[word[i]] = temp
                    node = temp
        else:
            node = MyNode(word[0], {})
            self.elements[word[0]] = node
            for i in xrange(1, len(word)):
                temp = MyNode(word[i], {})
                node.next[word[i]] = temp
                node = temp

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word in self.items:
            return True
        return False

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        if prefix:
            if prefix[0] not in self.elements:
                return False

            node = self.elements[prefix[0]]
            for i in range(1, len(prefix)):
                if prefix[i] not in node.next:
                    return False
                node = node.next[prefix[i]]

            return True

        return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
'''
