class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.store = nums[:]
        self.length = len(nums)-1

    def reset(self):
        """
        :rtype: List[int]
        """
        return self.store

    def shuffle(self):
        """
        :rtype: List[int]
        """
        nums = self.store[:]

        for i in range(self.length):
            swap_i = random.randint(i, self.length)
            nums[i], nums[swap_i] = nums[swap_i], nums[i]

        return nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
