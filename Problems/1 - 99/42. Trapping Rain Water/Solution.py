class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        n = len(height)

        #Option 3 - Stack
        consum = 0
        height_stack = []
        i = 0

        while i < n:
            # Stack not empty and current column higher than last wall in stack
            while len(height_stack) != 0 and height[i] > height[height_stack[-1]]:
                # Take the info out from the stack then pop out
                last_wall_index = height_stack[-1]
                height_stack.pop()
                # There is no column in stack higher than current column
                if len(height_stack) == 0:
                    break

                # Distance is current index minus the last column that after pop out.
                # And the distance that can used to re-calculate the missing part between 
                # last height wall
                distance = i - height_stack[-1] - 1
                # Find out which wall is loswest (between current and pre last column)
                min_column = min(height[i], height[height_stack[-1]])
                consum += distance * (min_column - height[last_wall_index])

            height_stack.append(i)
            #Move to next index
            i+=1

        return consum

        #Option 2 - Dynamic pointer method time O(n) space O(1)
        """
        consum = 0
        left = 1
        right = n-2
        left_max = 0
        right_max = 0

        #Pointer
        for _ in range(1, n):
            #Left wall is lower than right wall
            if height[left-1] < height[right+1]:
                # Record the most height wall for left side
                left_max = max(left_max, height[left-1])
                #Current column is lower than left wall, add water
                if left_max > height[left]:
                    consum += left_max - height[left]
                #Move from left to right
                left+=1
            #Right wall is lower than left wall or equal(right wall is same height as left)
            else:
                # Record the most height wall for left side
                right_max = max(right_max, height[right+1])
                #Current column is lower than right wall, add water
                if right_max > height[right]:
                    consum += right_max - height[right]
                #Move from right to left
                right-=1

        return consum
        """

        #Option 1 - Dynamic method time O(n) space O(n)
        """
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
        """
