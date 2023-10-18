class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        maximum = -1
        for i in range(len(arr)-1, -1, -1):
            if maximum < arr[i]:
                maximum, arr[i] = arr[i], maximum
            else:
                arr[i] = maximum

        return arr
