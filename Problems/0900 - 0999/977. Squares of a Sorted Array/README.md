# 977. Squares of a Sorted Array
### Tag: [Easy](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#easy-level), [Array](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#array), [Two Pointers](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#two-pointers), [Sorting](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#sorting)
---
<div class="px-5 pt-4"><div class="flex"></div><div class="xFUwe" data-track-load="description_content"><p>Given an integer array <code>nums</code> sorted in <strong>non-decreasing</strong> order, return <em>an array of <strong>the squares of each number</strong> sorted in non-decreasing order</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [-4,-1,0,3,10]
<strong>Output:</strong> [0,1,9,16,100]
<strong>Explanation:</strong> After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [-7,-3,2,3,11]
<strong>Output:</strong> [4,9,9,49,121]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code><span>1 &lt;= nums.length &lt;= </span>10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Squaring each element and sorting the new array is very trivial, could you find an <code>O(n)</code> solution using a different approach?</div></div>

---
<img src="Submit.png" width="700" height="215" />

### Solution

```python
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Option 3 - Two pointer, but only traversal once N, Time O(n)
        output = [0] * len(nums)
        left, right, i = 0, len(nums)-1, len(nums)-1
        while i != -1:
            if abs(nums[right]) > abs(nums[left]):
                output[i] = nums[right]**2
                right, i = right-1, i-1
            else:
                output[i] = nums[left]**2
                left, i = left+1, i-1

        return output

        # Option 2 - Two pointer, but needs traversal twice N, Time O(n)
        """
        length = len(nums)
        negative = positive = None
        negatives, positives = [], []

        for i in range(length):
            if nums[i] >= 0:
                negative, positive = i-1, i
                break
            negatives.append(nums[i]**2)

        if positive == None:
            return negatives[::-1]

        positives = [nums[i]**2 for i in range(positive, length)]
        
        length, positive, i = len(positives), 0, 0
        for i in range(len(nums)):
            if negative == -1:
                nums[i], positive = positives[positive], positive+1
            elif positive == length:
                nums[i], negative = negatives[negative], negative-1
            elif negatives[negative] < positives[positive]:
                nums[i], negative = negatives[negative], negative-1
            else:
                nums[i], positive = positives[positive], positive+1

        return nums
        """

        # Option 1
        """
        for i, num in enumerate(nums):
            nums[i] *= num

        nums.sort()
        return nums
        """
```
