class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        if length == 0:
            return [-1, -1]

        self.output = [-1, -1]
        
        def findTarget(left, right, updateLeft, updateRight):
            if left <= right:
                mid = (left + right) // 2
                temp = nums[mid]
                if temp > target:
                    right = mid-1
                elif temp < target:
                    left = mid+1
                else:
                    # Update the most left index
                    if updateLeft:
                        self.output[0] = mid
                        findTarget(left, mid-1, True, False)
                    # Update the most right index
                    elif updateRight:
                        self.output[1] = mid
                        findTarget(mid+1, right, False, True)
                    # self.output == [-1, -1]
                    else:
                        self.output = [mid, mid]
                        findTarget(left, mid-1, True, False)
                        findTarget(mid+1, right, False, True)
                    return

                findTarget(left, right, updateLeft, updateRight)

        findTarget(0, length-1, False, False)
                
        return self.output
