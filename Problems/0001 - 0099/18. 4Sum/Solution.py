class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(nums)
        nums = sorted(nums)

        last_val = nums[-1]
        last_index = length-1
        # *** For the lower N, it won't see the improvement ***
        bound_last_val = { n : last_val * n for n in range(2, 4+1) }

        self.output, self.store = [], []

        def get_N_Sum(goal, left, n):
            # *** For the lower N, it won't see the improvement ***
            if goal < nums[left] * n or goal > bound_last_val[n]:
                return
            """
            if goal < nums[left] * n or goal > last_val * n:
                return
            """

            # Since the list had been sorted, then used two pointer method to find the result
            if n == 2:
                right, temp = last_index, None
                while left < right:
                    temp = nums[left] + nums[right]
                    if temp > goal:
                        right -= 1
                    elif temp < goal:
                        left += 1
                    else:
                        temp = nums[left]
                        self.output.append(self.store + [temp, nums[right]])
                        left += 1
                        while left < right and nums[left] == temp:
                            left += 1
                
                return

            for i in range(left, length - n + 1):
                if nums[i] != nums[i-1] or i == left:
                    self.store.append(nums[i])
                    get_N_Sum( goal - nums[i], i+1, n-1 )
                    self.store.pop()
        
        get_N_Sum(target, 0, 4)

        return self.output
