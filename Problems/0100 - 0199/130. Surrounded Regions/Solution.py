class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        self.m = len(board)
        self.n = len(board[0])
        rows = range(self.m)
        cols = range(self.n)

        self.alives = set()

        def markO(neighbors):
            for x, y in neighbors:
                if x == -1 or x == self.m or y == -1 or y == self.n or (x,y) in self.alives:
                    continue 
                elif board[x][y] == 'O':
                    self.alives.add((x, y))
                    markO([(x-1, y), (x, y-1), (x, y+1), (x+1, y)])

        # First and Last Rows
        last = self.m-1
        for y in cols:
            if board[0][y] == 'O' and (0, y) not in self.alives:
                self.alives.add((0, y))
                markO([(1, y)])
            if board[last][y] == 'O' and (last, y) not in self.alives:
                self.alives.add((last, y))
                markO([(last-1, y)])

        # First and Last Cols
        last = self.n-1
        for x in rows:
            if board[x][0] == 'O' and (x, 0) not in self.alives:
                self.alives.add((x, 0))
                markO([(x, 1)])
            if board[x][last] == 'O' and (x, last) not in self.alives:
                self.alives.add((x, last))
                markO([(x, last-1)])

        for x in rows:
            for y in cols:
                if board[x][y] == 'O' and (x, y) not in self.alives:
                    board[x][y] = 'X'
