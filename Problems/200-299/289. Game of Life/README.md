# 289. Game of Life
### Tag: [Medium](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#medium-level), [Array](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#array), [Matrix](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#matrix)
---
<div class="px-5 pt-4"><div class="flex"></div><div class="_1l1MA" data-track-load="description_content"><p>According to&nbsp;<a href="https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life" target="_blank">Wikipedia's article</a>: "The <b>Game of Life</b>, also known simply as <b>Life</b>, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."</p>

<p>The board is made up of an <code>m x n</code> grid of cells, where each cell has an initial state: <b>live</b> (represented by a <code>1</code>) or <b>dead</b> (represented by a <code>0</code>). Each cell interacts with its <a href="https://en.wikipedia.org/wiki/Moore_neighborhood" target="_blank">eight neighbors</a> (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):</p>

<ol>
	<li>Any live cell with fewer than two live neighbors dies as if caused by under-population.</li>
	<li>Any live cell with two or three live neighbors lives on to the next generation.</li>
	<li>Any live cell with more than three live neighbors dies, as if by over-population.</li>
	<li>Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.</li>
</ol>

<p><span>The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the <code>m x n</code> grid <code>board</code>, return <em>the next state</em>.</span></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/26/grid1.jpg" style="width: 562px; height: 322px;">
<pre><strong>Input:</strong> board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
<strong>Output:</strong> [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/26/grid2.jpg" style="width: 402px; height: 162px;">
<pre><strong>Input:</strong> board = [[1,1],[1,0]]
<strong>Output:</strong> [[1,1],[1,1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n == board[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 25</code></li>
	<li><code>board[i][j]</code> is <code>0</code> or <code>1</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong></p>

<ul>
	<li>Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.</li>
	<li>In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?</li>
</ul>
</div></div>

---
<img src="Submit.png" width="700" height="215" />

### Solution

```python
class Solution(object):
    def checkNeighbors(self, board, neighbors, live):
        lives = 0
        for x, y in neighbors:
            if x == -1 or x == self.m or y == -1 or y == self.n:
                continue
            if board[x][y] > 0:
                lives += 1

        # No matter the cell is live or dead, if there have 3 neighbors alive
        if lives == 3:
            return True
        # If the cell is live and there have 2 neighbors alive
        elif live == 1 and lives == 2:
            return True

        return False
    
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.m = len(board)
        self.n = len(board[0])

        for x in range(self.m):
            for y in range(self.n):
                top = x-1
                bottom = x+1
                left = y-1
                right = y+1
                neighbors = [   (top,left),         # Top Left
                                (top,y),            # Top
                                (top,right),        # Top-Right
                                (x,left),           # Left
                                (x,right),          # Right
                                (bottom,left),      # Bottom Left
                                (bottom,y),         # Bottom
                                (bottom,right)  ]   # Bottom Right
                
                # EVEN and ODD method:
                # How to identify the Previous State is 1(live) or 0(dead)?
                # Let 1(live) means > 0 ==> POSITIVE
                # Let 0(dead) means !> 0 ==> NOT POSITIVE
                # If neighbor > 0 ==> POSITIVE means Previous State: 1(live)
                # Else ==> NOT POSITIVE means Previous State: 0(dead)
                # We can make a logic for restore the previous state
                # Previous: 0 & Next: 1 ==> -1 ( -1 % 2 = 1 )
                # Previous: 0 & Next: 0 ==>  0 (  0 % 2 = 0 )
                # Previous: 1 & Next: 1 ==>  1 (  1 % 2 = 1 )
                # Previous: 1 & Next: 0 ==>  2 (  2 % 2 = 0 )

                # If next state is 1(live)
                if self.checkNeighbors(board, neighbors, board[x][y]):
                    # Previous: 0 & Next: 1 ==> -1 ( -1 % 2 = 1 )
                    if board[x][y] == 0:
                        board[x][y] = -1
                    # Previous: 1 & Next: 1 ==>  1 (  1 % 2 = 1 ) 
                    # Previous: 1 ==> 1, So NO change
                    
                # If next state is 0(dead)
                else:
                    # Previous: 1 & Next: 0 ==>  2 (  2 % 2 = 0 )
                    if board[x][y] == 1:
                        board[x][y] = 2
                    # Previous: 0 & Next: 0 ==>  0 (  0 % 2 = 0 )
                    # Previous: 0 ==> 0, So NO change

        for x in range(self.m):
            for y in range(self.n):
                board[x][y] %= 2

"""
                # POSTIVE -1 AND NOT POSITIVE +1 method:
                # How to identify the Previous State is 1(live) or 0(dead)?
                # Let 1(live) means > 0 ==> POSITIVE
                # Let 0(dead) means !> 0 ==> NOT POSITIVE
                # If neighbor > 0 ==> POSITIVE means Previous State: 1(live)
                # Else ==> NOT POSITIVE means Previous State: 0(dead)
                # We can make a logic for restore the previous state
                # Previous: 0 & Next: 1 ==>  0 (NOT POSITIVE: +1 ==> 0 + 1 = 1)
                # Previous: 0 & Next: 0 ==> -1 (NOT POSITIVE: +1 ==> -1 + 1 = 0)
                # Previous: 1 & Next: 1 ==>  2 (POSITIVE: -1 ==> 2 - 1 = 1)
                # Previous: 1 & Next: 0 ==>  1 (POSITIVE: -1 ==> 1 - 1 = 0)

                # If next state is 1(live)
                if self.checkNeighbors(board, neighbors, board[x][y]):
                    # Previous: 1 & Next: 1 ==>  2 (POSITIVE: -1 ==> 2 - 1 = 1)
                    if board[x][y] == 1:
                        board[x][y] = 2
                    # Previous: 0 & Next: 1 ==>  0 (NOT POSITIVE: +1 ==> 0 + 1 = 1) 
                    # Previous: 0 ==> 0, So NO change
                    
                # If next state is 0(dead)
                else:
                    # Previous: 0 & Next: 0 ==> -1 (NOT POSITIVE: +1 ==> -1 + 1 = 0)
                    if board[x][y] == 0:
                        board[x][y] = -1
                    # Previous: 1 & Next: 0 ==>  1 (POSITIVE: -1 ==> 1 - 1 = 0)
                    # Previous: 1 ==> 1, So NO change

        for x in range(self.m):
            for y in range(self.n):
                if board[x][y] > 0:
                    board[x][y] -= 1
                else:
                    board[x][y] += 1 
"""
```
