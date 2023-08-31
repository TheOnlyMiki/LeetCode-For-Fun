class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        last_index = len(nums) - 1
        short_jumps = 0
        max_reachable_position = 0
        position = 0

        if last_index == 0:
            return short_jumps

        for i, jump in enumerate(nums[:last_index]):
            if max_reachable_position < i + jump:
                max_reachable_position = i + jump
            
            if position == i:
                position = max_reachable_position
                short_jumps += 1
            
        return short_jumps
