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

        while left != right:
            area = distance * min(height[left], height[right])
            if max_record < area:
                max_record = area

            # Initial next iteration
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            distance -=1

        return max_record
