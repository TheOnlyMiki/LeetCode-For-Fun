"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
import numpy as np
class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        n = len(grid)
        if n == 1:
            return Node(grid[0][0], True)

        grid = np.array(grid)

        def checkAllSame(i, j, x, y):
            temp = grid[ i:x, j:y ]
            consum = np.sum(temp)
            if consum == 0:
                return Node(False, True)
            if consum == temp.size:
                return Node(True, True)

            current = Node(False, False)

            mid_x, mid_y = (i + x) / 2, (j + y) / 2
            current.topLeft = checkAllSame(i, j, mid_x, mid_y)
            current.topRight = checkAllSame(i, mid_y, mid_x, y)
            current.bottomLeft = checkAllSame(mid_x, j, x, mid_y)
            current.bottomRight = checkAllSame(mid_x, mid_y, x, y)

            return current

        return checkAllSame(0, 0, n, n)
