class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        length = len(flowerbed)

        flowerbed.append(0)
        i = 0

        while i < length:
            if 0 == flowerbed[i] == flowerbed[i-1] == flowerbed[i+1]:
                n -= 1
                i += 1
            
            i += 1
        
        return n < 1
