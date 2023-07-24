class RandomizedSet(object):

    def __init__(self):
        self.q = []
        self.length = 0

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.q:
            self.q.append(val)
            return True
        else:
            return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        try:
            self.q.remove(val)
            return True
        except:
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
