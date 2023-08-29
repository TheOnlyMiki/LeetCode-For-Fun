# 42. Trapping Rain Water
### Tag: [Hard](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#hard-level), [Array](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#array), [Two Pointers](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#two-pointers), [Dynamic Programming](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#dynamic-programming), [Stack](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#stack)
---
<div class="px-5 pt-4"><div class="flex"></div><div class="_1l1MA" data-track-load="description_content"><p>Given <code>n</code> non-negative integers representing an elevation map where the width of each bar is <code>1</code>, compute how much water it can trap after raining.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png" style="width: 412px; height: 161px;">
<pre><strong>Input:</strong> height = [0,1,0,2,1,0,1,3,2,1,2,1]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> height = [4,2,0,3,2,5]
<strong>Output:</strong> 9
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == height.length</code></li>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= height[i] &lt;= 10<sup>5</sup></code></li>
</ul>
</div></div>

---
<img src="Submit.png" width="700" height="215" />

### Solution

```python
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
```
