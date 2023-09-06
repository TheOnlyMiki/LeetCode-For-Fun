class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Option 2 - Space O(1)
        left, right = 0, len(numbers)-1
        temp = None
        while left < right:
            temp = numbers[left] + numbers[right]
            if temp < target:
                left += 1
            elif temp > target:
                right -= 1
            else:
                return [left+1, right+1]

        # Option 1 - Space O(n)
        """
        diff = {}
        
        for i, number in enumerate(numbers):
            if number in diff:
                return [diff[number], i+1]
            diff[target - number] = i+1

        return None
        """
