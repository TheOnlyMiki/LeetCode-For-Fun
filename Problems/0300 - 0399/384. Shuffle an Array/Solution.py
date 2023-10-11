class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin = nums[:]
        self.store = nums[:]

    def reset(self):
        """
        :rtype: List[int]
        """
        return self.origin

    def shuffle(self):
        """
        :rtype: List[int]
        """
        length = len(self.store)-1
        for i in range(length):
            swap_i = random.randint(i, length)
            self.store[i], self.store[swap_i] = self.store[swap_i], self.store[i]

        return self.store


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
