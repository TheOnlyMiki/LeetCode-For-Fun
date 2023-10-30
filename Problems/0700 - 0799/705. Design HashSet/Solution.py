class MyHashSet(object):

    def __init__(self):
        self.store = [None] * 1000

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key):
            return

        hashnum1 = key % 1000
        if not self.store[hashnum1]:
            self.store[hashnum1] = [None] * 100

        if not self.store[hashnum1][key % 100]:
            self.store[hashnum1][key % 100] = [key]
        else:
            self.store[hashnum1][key % 100].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key):
            self.store[key % 1000][key % 100].remove(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return False if not self.store[key % 1000] else (True if key in self.store[key % 1000][key % 100] else False)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
