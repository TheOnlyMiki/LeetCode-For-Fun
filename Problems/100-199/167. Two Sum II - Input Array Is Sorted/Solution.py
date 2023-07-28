class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        diff = {}
        
        for i, number in enumerate(numbers):
            if number in diff:
                return [diff[number], i+1]
            diff[target - number] = i+1

        return None
