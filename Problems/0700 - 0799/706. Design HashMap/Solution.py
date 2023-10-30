class MyHashMap(object):

    def __init__(self):
        self.storeKeys = [None] * 1000

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        hashnum1 = key % 1000
        if not self.storeKeys[hashnum1]:
            self.storeKeys[hashnum1] = [None] * 100

        hashnum2 = key % 100
        if self.storeKeys[hashnum1][hashnum2]:
            if key in self.storeKeys[hashnum1][hashnum2][0]:
                self.storeKeys[hashnum1][hashnum2][1][ self.storeKeys[hashnum1][hashnum2][0].index(key) ] = value
            else:
                self.storeKeys[hashnum1][hashnum2][0].append(key)
                self.storeKeys[hashnum1][hashnum2][1].append(value)
        else:
            self.storeKeys[hashnum1][hashnum2] = [[key], [value]]

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        hashnum1 = key % 1000
        if self.storeKeys[hashnum1]:
            hashnum2 = key % 100
            if self.storeKeys[hashnum1][hashnum2]:
                if key in self.storeKeys[hashnum1][hashnum2][0]:
                    return self.storeKeys[hashnum1][hashnum2][1][ self.storeKeys[hashnum1][hashnum2][0].index(key) ]

        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hashnum1 = key % 1000
        if self.storeKeys[hashnum1]:
            hashnum2 = key % 100
            if key in self.storeKeys[hashnum1][hashnum2][0]:
                index = self.storeKeys[hashnum1][hashnum2][0].index(key)
                self.storeKeys[hashnum1][hashnum2][0].pop(index)
                self.storeKeys[hashnum1][hashnum2][1].pop(index)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
