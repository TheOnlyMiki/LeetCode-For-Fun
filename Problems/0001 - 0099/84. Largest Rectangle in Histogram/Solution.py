class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Option 2
        output = 0
        stack = [-1]
        heights.append(0)
        for i, h in enumerate(heights):
            while heights[stack[-1]] > h:
                height = heights[stack.pop()]
                if output < height * (i - stack[-1] - 1):
                    output = height * (i - stack[-1] - 1)
            
            stack.append(i)

        return output

        # Option 1
        """
        output = 0
        stack = [(0, -1)]
        for i, h in enumerate(heights):
            while stack[-1][0] > h:
                height = stack.pop()[0]
                area = height * (i - 1 - stack[-1][1])
                if output < area:
                    output = area
            
            stack.append((h, i))

        while stack[-1][0] > 0:
            height = stack.pop()[0]
            area = height * (len(heights) - 1 - stack[-1][1])
            if output < area:
                output = area

        return output
        """
