class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        self.output = []
        def dfs(start, store):
            self.output.append(store)
            for i in range(start, length):
                dfs(i+1, store + [nums[i]])
        
        dfs(0, [])
        return self.output
