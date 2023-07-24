class RandomizedSet(object):

    def __init__(self):
        self.q = []
        self.find = {}
        self.length = 0

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.find:
            self.q.append(val)
            self.find[val] = self.length
            self.length+=1
            return True
        else:
            return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.find:
            index_remove = self.find[val]
            self.find[self.q[-1]] = index_remove
            self.q[index_remove] = self.q[-1]
            del self.find[val]
            self.q.pop()
            self.length-=1
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.q)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
