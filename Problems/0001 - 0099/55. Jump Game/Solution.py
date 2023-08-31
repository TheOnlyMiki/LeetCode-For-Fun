class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        #Option 2
        max_reachable_position = 0

        for i, jump in enumerate(nums):
            if i > max_reachable_position:
                return False
                
            if i + jump > max_reachable_position:
                max_reachable_position = i + jump
        
        return True

        #Option 1
        """
        back_position = len(nums)-1
        
        for i in range(back_position-1, -1, -1):
            if i + nums[i] >= back_position:
                back_position = i

        if back_position == 0:
            return True
        
        return False
        """

"""
#Recursion backward method - slow and one step by step check
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
"""
