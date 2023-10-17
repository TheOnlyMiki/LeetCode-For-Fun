class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        # Option 2 - In place
        for i in range(len(arr)-2, -1, -1):
            if arr[i] == 0:
                arr[i+1:] = arr[i:-1]

        """
        length = len(arr)-1
        for i in range(length, -1, -1):
            if arr[i] == 0:
                for i2 in range(length, i, -1):
                    arr[i2] = arr[i2-1]
        """

        # Option 1 - extra spaces
        """
        i, length, output = 0, len(arr), []
        while len(output) < length:
            if arr[i] == 0:
                output.append(0)

            output.append(arr[i])
            i += 1

        arr[:] = output[:length]
        """
