class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        record = set()
        for num in nums:
            if num in record:
                return True
            record.add(num)

        return False
