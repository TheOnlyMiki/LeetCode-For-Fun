class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Option 2 - BF method with memorize
        record = {}
        
        def dfs(record, i, consum):
            if (i, consum) in record:
                return record[(i, consum)]

            if i == -1:
                return 1 if consum == target else 0

            record[(i, consum)] = dfs(record, i-1, consum + nums[i]) + dfs(record, i-1, consum - nums[i])
            return record[(i, consum)]      

        return dfs(record, len(nums)-1, 0)

        # Option 1 - BF method, cannot pass
        """
        self.output = 0
        
        def dfs(consum, i):
            if i == -1:
                if consum == target:
                    self.output += 1
                return

            dfs(consum + nums[i], i-1)
            dfs(consum - nums[i], i-1)

        dfs(0,len(nums)-1)
        return self.output
        """
