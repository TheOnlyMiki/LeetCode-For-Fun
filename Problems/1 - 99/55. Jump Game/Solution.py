class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last_index = len(nums) - 1

        prejump = {0:0}
        for i, jump in enumerate(nums[:last_index]):
            if i + jump in prejump:
                prejump[i + jump].append(i)
            else:
                prejump[i + jump] = [i]

        print(prejump)  

        if max(prejump.keys()) >= last_index:
            return True
        
        return False    


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
