class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        length = len(nums) - 1
        if length == 0:
            return True if target == nums[0] else False

        left, right = 0, length
        mid = current = None

        while left <= right:
            mid = (left + right) // 2
            current = nums[mid]
            if current == target:
                return True

            if nums[left] == current == nums[right]:
                left += 1
                right -= 1
            elif current >= nums[left]:
                if target >= nums[left] and target < current:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if target <= nums[right] and target > current:
                    left = mid+1
                else:
                    right = mid-1

        return False
