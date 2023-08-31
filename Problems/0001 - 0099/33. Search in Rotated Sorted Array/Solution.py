class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Option 3 - Find out the rotated index
        length = len(nums) - 1
        if length == 0:
            return 0 if target == nums[0] else -1

        left, right = 0, length
        mid = current = None

        if nums[left] > nums[right]:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= nums[right]:
                    left = mid+1
                else:
                    right = mid

            left, right = (right, length) if nums[length] >= target else (0, right-1)

        while left <= right:
            mid = (left + right) // 2
            current = nums[mid]
            if target < current:
                right = mid-1
            elif target > current:
                left = mid+1
            else:
                return mid

        return -1

        # Option 2 - Binary search
        """
        length = len(nums) - 1
        if length == 0:
            return 0 if target == nums[0] else -1

        left, right = 0, length
        current = None

        while left <= right:
            mid = (left + right) // 2
            current = nums[mid]
            if current == target:
                return mid
            if current >= nums[left]:
                if target >= nums[left] and target < current:
                    right = mid-1
                else:
                    left = mid+1
            else:
                if target <= nums[right] and target > current:
                    left = mid+1
                else:
                    right = mid-1

        return -1
        """

        # Option 1 - Bad design binary search, slowly
        """
        length = len(nums) - 1
        if length == 0:
            return 0 if target == nums[0] else -1

        left, right = 0, length
        current = None
        rotated = True if nums[left] > nums[right] else False

        while left <= right:
            mid = (left + right) // 2
            current = nums[mid]
            if target < current:
                # Rotated List
                if rotated:
                    if current <= nums[right]:
                        right = mid-1
                    elif target <= nums[right]:
                        left = mid+1
                        continue
                # Not Rotated List
                right = mid-1
            elif target > current:
                # Rotated List
                if rotated:
                    if nums[left] <= current:
                        left = mid+1
                    elif target >= nums[left]:
                        right = mid-1
                        continue
                # Not Rotated List
                left = mid+1
            else:
                return mid

        return -1
        """
