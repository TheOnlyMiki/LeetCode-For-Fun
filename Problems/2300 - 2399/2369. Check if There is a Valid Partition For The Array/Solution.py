class Solution(object):
    def validPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        record = [False] * (length+1)
        record[length] = True

        previou1, previou2 = nums[1], nums[0]
        record[1] = True if previou1 == previou2 else False

        for i in range(2, length):
            record[i] = (
                (record[i-2] and nums[i] == previou1) or \
                (record[i-3] and (nums[i] == previou1 == previou2 or nums[i] == previou1+1 == previou2+2))
            )
            
            previou2 = previou1
            previou1 = nums[i]

        return record[length-1]
