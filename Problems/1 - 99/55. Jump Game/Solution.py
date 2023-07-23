class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) == 1:
            return True

        return self.checkReachable(nums, len(nums)-2, 1)
        
    def checkReachable(self, nums, position, distance):
        print(distance, position, nums[position])
        if position == 0:
            if nums[position] < distance:
                return False
            else:
                return True
        
        if nums[position] < distance:
            return self.checkReachable(nums, position-1, distance+1)
        else:
            return self.checkReachable(nums, position-1, 1)
