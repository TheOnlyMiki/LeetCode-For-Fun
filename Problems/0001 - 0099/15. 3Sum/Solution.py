class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Option 2
        length = len(nums)
        nums = sorted(nums)

        # *** For the lower N, it won't see the improvement ***
        #bound_last_val = { n : nums[-1] * n for n in range(2, 3+1) }
        last_val = nums[-1]
        last_index = length-1

        self.output, self.store = [], []

        def get_N_Sum(target, left, n):
            # *** For the lower N, it won't see the improvement ***
            """
            if target < nums[left] * n or target > bound_last_val[n]:
                return
            """
            if target < nums[left] * n or target > last_val * n:
                return

            # Since the list had been sorted, then used two pointer method to find the result
            if n == 2:
                right, temp = last_index, None
                while left < right:
                    temp = nums[left] + nums[right]
                    if temp > target:
                        right -= 1
                    elif temp < target:
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
                    get_N_Sum( target - nums[i], i+1, n-1 )
                    self.store.pop()
        
        get_N_Sum(0, 0, 3)

        return self.output

        # Option 1
        """
        count = {}
        output = set()

        # Count the number of occurrences - O(n)
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        zero_exist = False
        if 0 in count:
            zero_exist = True
            if count[0] > 2:
                output.add((0,0,0))
            del count[0]

        record_count = count.keys() #List
        record_count_len = len(record_count)
            
        while record_count_len != 0:
            a = record_count[0]
            del record_count[0]
            record_count_len -= 1

            if zero_exist and -a in count:
                output.add(tuple(sorted([-a,0,a])))

            # a + b + c = 0 -> c = 0 - a - b
            for b in record_count:
                c = -a - b
                if c in count:
                    if a == b:
                        if count[a] > 1:
                            output.add(tuple(sorted([a,a,c])))
                    elif b == c:
                        if count[b] > 1:
                            output.add(tuple(sorted([a,b,b])))
                    elif a == c:
                        if count[a] > 1:
                            output.add(tuple(sorted([a,a,b])))
                    else:
                        output.add(tuple(sorted([a,b,c])))

        return output
        """
