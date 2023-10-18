class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False

        decrease = 0
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                decrease = i-1
                break

        if decrease == 0 or decrease == len(arr)-1:
            return False

        for i in range(decrease+1, len(arr)):
            if arr[i] >= arr[i-1]:
                return False

        return True
