class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        row, col = len(maze), len(maze[0])
        moves = [(0,1), (1,0), (0,-1), (-1,0)]
        maze[entrance[0]][entrance[1]] = None

        record = []
        for x, y in moves:
            x, y = entrance[0] + x, entrance[1] + y
            if -1 < x < row and -1 < y < col and maze[x][y] == '.':
                maze[x][y] = None
                record.append((x, y))
        
        step = 1
        while record:
            temp = []
            for x, y in record:
                for new_x, new_y in moves:
                    new_x, new_y = x + new_x, y + new_y
                    if new_x == -1 or new_x == row or new_y == -1 or new_y == col:
                        return step
                    if maze[new_x][new_y] == '.':
                        maze[new_x][new_y] = None
                        temp.append((new_x, new_y))

            step += 1
            record = temp

        return -1
