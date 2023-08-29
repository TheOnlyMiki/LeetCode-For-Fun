# 542. 01 Matrix
### Tag: [Medium](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#medium-level), [Array](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#array), [Dynamic Programming](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#dynamic-programming), [Matrix](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#matrix), [Breadth-First Search](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#breadth-first-search)
---
<div class="px-5 pt-4"><div class="flex"></div><div class="xFUwe" data-track-load="description_content"><p>Given an <code>m x n</code> binary matrix <code>mat</code>, return <em>the distance of the nearest </em><code>0</code><em> for each cell</em>.</p>

<p>The distance between two adjacent cells is <code>1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/01-1-grid.jpg" style="width: 253px; height: 253px;">
<pre><strong>Input:</strong> mat = [[0,0,0],[0,1,0],[0,0,0]]
<strong>Output:</strong> [[0,0,0],[0,1,0],[0,0,0]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/01-2-grid.jpg" style="width: 253px; height: 253px;">
<pre><strong>Input:</strong> mat = [[0,0,0],[0,1,0],[1,1,1]]
<strong>Output:</strong> [[0,0,0],[0,1,0],[1,2,1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>4</sup></code></li>
	<li><code>mat[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
	<li>There is at least one <code>0</code> in <code>mat</code>.</li>
</ul>
</div></div>

---
<img src="Submit.png" width="700" height="215" />

### Solution

```python
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        cols1, cols2 = range(n), range(n-1, -1, -1)
        maximum = m + n
        record1 = [maximum]*(n+1)
        record2 = [maximum]*(n+1)
        temp1 = temp2 = pre_i = None
    
        for i in range(m):
            record2[:n] = mat[i]
            for j in cols1:
                if mat[i][j] > 0:
                    mat[i][j] = record2[j] = min(record1[j], record2[j-1]) + 1

            record1[:] = record2[:]
        
        record1 = [maximum]*(n+1)
        for i in range(m-1, -1, -1):
            record2[:n] = mat[i]
            for j in cols2:
                if mat[i][j] > 0:
                    mat[i][j] = record2[j] = min(mat[i][j], min(record1[j], record2[j+1]) + 1)

            record1[:] = record2[:]
        
        return mat

        # Option 1 - No idea why it was wrong.
        """
        m, n = len(mat), len(mat[0])
        cols = range(n)
        maximum = m + n
        record1 = [maximum]*(n+1)
        record2 = [maximum]*(n+1)
        pre_i = cur_i = pre_j = cur_j = next_i = next_j = None
    
        for i in range(m):
            record2[:n] = mat[i]
            for j in cols:
                if mat[i][j] > 0:
                    mat[i][j] = record2[j] = min(record1[j], record2[j-1]) + 1
                
                pre_i, cur_i, pre_j, cur_j, next_i, next_j = i-1, i, j-1, j, i, j
                while next_i >= 0 and next_j >= 0:
                    while pre_i >= 0 and mat[pre_i][next_j] > mat[cur_i][next_j] + 1:
                        mat[pre_i][next_j] = mat[cur_i][next_j] + 1
                        cur_i = pre_i
                        pre_i -= 1

                    while pre_j >= 0 and mat[next_i][pre_j] > mat[next_i][cur_j] + 1:
                        mat[next_i][pre_j] = mat[next_i][cur_j] + 1
                        cur_j = pre_j
                        pre_j -= 1

                    pre_i, pre_j = next_i-1, next_j-1
                    cur_i, cur_j = pre_i+1, pre_j+1
                    next_i -= 1
                    next_j -= 1

            record1[:] = record2[:]
        
        return mat
        """
```
