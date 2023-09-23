# 216. Combination Sum III
### Tag: [Medium](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#medium-level), [Array](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#array), [Backtracking](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#backtracking)
---
<div class="px-5 pt-4"><div class="flex"></div><div class="xFUwe" data-track-load="description_content"><p>Find all valid combinations of <code>k</code> numbers that sum up to <code>n</code> such that the following conditions are true:</p>

<ul>
	<li>Only numbers <code>1</code> through <code>9</code> are used.</li>
	<li>Each number is used <strong>at most once</strong>.</li>
</ul>

<p>Return <em>a list of all possible valid combinations</em>. The list must not contain the same combination twice, and the combinations may be returned in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> k = 3, n = 7
<strong>Output:</strong> [[1,2,4]]
<strong>Explanation:</strong>
1 + 2 + 4 = 7
There are no other valid combinations.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> k = 3, n = 9
<strong>Output:</strong> [[1,2,6],[1,3,5],[2,3,4]]
<strong>Explanation:</strong>
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> k = 4, n = 1
<strong>Output:</strong> []
<strong>Explanation:</strong> There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 &gt; 1, there are no valid combination.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= k &lt;= 9</code></li>
	<li><code>1 &lt;= n &lt;= 60</code></li>
</ul>
</div></div>

---
<img src="Submit.png" width="700" height="215" />

### Solution

```python
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # Option 2 - Fast
        self.record = []
        def getCombination(i, remain, k):
            if k == 0:
                if remain == 0:
                    self.output.append(self.record[:])
                return
            
            for num in range(i, 10):
                if remain - num < 0:
                    return
                
                self.record.append(num)
                getCombination(num+1, remain-num, k-1)
                self.record.pop()

        self.output = []
        getCombination(1, n, k)

        return self.output

        # Option 1 - Using less space, but time complexity were too bigger(so slowly)
        """
        represent = [1,2,3,4,5,6,7,8,9]
        record = set()
        visit = {1,2,3,4,5,6,7,8,9}

        def getCombination(remain, k):
            if k == 1:
                if remain in visit:
                    temp = record | {remain}
                    if temp not in self.output:
                        self.output.append(temp)
                    return
            else:
                for num in represent:
                    if num in visit and remain - num > 0:
                        visit.remove(num)
                        record.add(num)
                        getCombination(remain - num, k-1)
                        record.remove(num)
                        visit.add(num)

        self.output = []
        getCombination(n, k)

        return self.output
        """
```
