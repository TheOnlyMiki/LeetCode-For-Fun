class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Option 2
        count = {}
        
        for value in nums:
            if value in count:
                count[value] += 1
            else:
                count[value] = 1
        
        return max(count, key=count.get)

        #Option 1
        """
        count = {}
        n = len(nums)
        majority = int((n+1)/2)
        
        for i in range(majority):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1

        if majority not in count.values():
            for i in range(majority, n):
                if nums[i] in count:
                    count[nums[i]] += 1
                else:
                    count[nums[i]] = 1
        
        return max(count, key=count.get)"""
