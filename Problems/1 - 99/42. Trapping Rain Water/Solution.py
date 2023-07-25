class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        n = len(height)

        #Option 1 - Dynamic time O(n) space O(n)
        left_height = [0] * n
        right_height = [0] * n
        consum = 0

        #Left
        for i in range(1, n):
            left_height[i] = max(left_height[i-1], height[i-1])
        #Right
        for i in range(n-2, -1, -1):
            right_height[i] = max(right_height[i+1], height[i+1])
        #Calculate 
        for i in range(1, n):
            min_wall = min(left_height[i], right_height[i])
            if min_wall > height[i]:
                consum += min_wall - height[i]

        return consum
