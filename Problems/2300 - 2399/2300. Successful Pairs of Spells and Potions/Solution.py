class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        # Option 3
        """
        potions = sorted(potions)
        length = len(potions)
        
        output = []
        for num in spells:
            output.append(length - bisect_left(potions, (success + num - 1) // num))

        return output
        """

        # Option 2
        potions = sorted(potions, reverse=True)
        length = len(potions)

        for i, num in enumerate(potions):
            potions[i] = (success - 1) / num + 1

        def binarySearch(num):
            left, right = 0, length
            while left < right:
                mid = (left + right) // 2
                if potions[mid] > num:
                    right = mid
                else:
                    left = mid + 1

            return left
        
        output = []
        for num in spells:
            # Bisect_left would be same speed as Option 3
            #output.append(bisect_left(potions,num+1))
            output.append(binarySearch(num))

        return output

        # Option 1
        """
        potions = sorted(potions)
        length = len(potions)

        def binarySearch(num):
            left, right = 0, length
            while left < right:
                mid = (left + right) // 2
                temp = potions[mid] * num
                if temp < success:
                    left = mid + 1
                else:
                    right = mid

            return length - left
        
        output = []
        for num in spells:
            output.append(binarySearch(num))

        return output
        """
