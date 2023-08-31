class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Option 2
        def insertMostLeft(a, x):
            left, right, mid = 0, len(a), None
            while left < right:
                mid = (left + right) / 2
                if a[mid] < x: 
                    left = mid + 1
                else: 
                    right = mid
            return left

        record = []
        temp = None

        for num in nums:
            if not record or record[-1] < num:
                record.append(num)
            else:
                record[insertMostLeft(record, num)] = num
        
        return len(record)

        # Option 1
        """
        record = [1] * len(nums)
        temp = None

        for i, num in enumerate(nums):
            temp = -1
            for j in xrange(i):
                if nums[j] < num and temp < record[j]:
                    temp = record[j]

            record[i] = temp+1 if temp != -1 else 1
        
        return max(record)
        """
