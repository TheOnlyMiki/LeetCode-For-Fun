class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        diff = {}
        output = None
        
        for i, number in enumerate(numbers):
            if number in diff:
                output = [diff[number], i+1]
                break
            diff[target - number] = i+1

        return output
