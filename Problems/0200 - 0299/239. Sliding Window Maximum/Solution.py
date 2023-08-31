from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Option 2 - Queue with Math method
        output = []
        queue = deque()
        num = None

        for i in range(k-1):
            num = nums[i]
            while queue and nums[queue[-1]] < num:
                queue.pop()
            queue.append(i)
        
        for i in range(k-1, len(nums)):
            num = nums[i]

            while queue and nums[queue[-1]] < num:
                queue.pop()

            queue.append(i)
            output.append(nums[queue[0]])

            if queue[0] == i-k+1:
                queue.popleft()

        return output

        # Option 1 - Queue with Max() method, but can't pass cause max method take O(k*n)
        """
        output = []
        queue = deque()

        for i, num in enumerate(nums):
            if i < k:
                queue.append(num)
            else:
                output.append( max(queue) )
                queue.popleft()
                queue.append(num)

        output.append(max(queue))
        return output
        """
