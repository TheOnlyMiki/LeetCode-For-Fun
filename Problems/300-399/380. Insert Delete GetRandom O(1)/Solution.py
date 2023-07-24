class RandomizedSet(object):

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            return False
        else:
            self.list.append(val)
            self.dict[val] = len(self.list)-1 #record idx in dict; will help in O(1) delete
            return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        #idea is to pop last element always coz that's constant time
        #thus, we need to update index of last element to that idx we want to delete in dict
        #and at that idx, put the last element and now in this way we deleted the idx we wanna by
        #replacing and then last element will be redundant and will be popped
        if val not in self.dict:
            return False
        else:
            idx_to_delete = self.dict[val]
            last_element = self.list[-1]
            self.dict[last_element] = idx_to_delete
            self.list[idx_to_delete] = last_element
            del self.dict[val]
            self.list.pop()
            return True

    def getRandom(self):
        """
        :rtype: int
        """
        return choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
