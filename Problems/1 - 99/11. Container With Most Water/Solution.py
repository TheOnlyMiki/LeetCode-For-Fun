class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        distance = len(height) - 1
        left = 0
        right = distance
        max_record = 0
        higher = max(height)

        while left < right:
            area = min(height[left], height[right]) * distance
            if max_record < area:
                max_record = area
            
            if higher * distance < max_record:
                return max_record

            # Initial next iteration
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            distance -=1

        return max_record
