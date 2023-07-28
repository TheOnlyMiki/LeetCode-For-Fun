class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        distance = len(height)
        left = 0
        right = distance-1
        max_record = 0

        while left != right:
            distance -=1

            max_record = max(max_record, distance * min(height[left], height[right]))

            # Initial next iteration
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_record
