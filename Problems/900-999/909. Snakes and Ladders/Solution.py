class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        goal = n*n
        moves = range(1, 7)
        direction_left = n%2

        def getIndex(pos):
            x = n - 1 - ((pos-1) // n)
            y = (pos-1) % n
            if x%2 == direction_left:
                y = n - 1 - y
            return x, y

        # Option 2 - BFS without 'deque'
        actions = [(0, 1)]
        record = {(0, 1)}
        next_actions = None

        while actions:
            next_actions = []
            for step, position in actions:
                for move in moves:
                    pos = position + move
                    x, y = getIndex(pos)
                    if (x, y) not in record:
                        pos = (pos if board[x][y] == -1 else board[x][y])
                        if pos == goal:
                            return step + 1
                        record.add((x, y))
                        next_actions.append((step + 1, pos))
                    
            actions = next_actions

        return -1

        # Option 1 - BFS with python queue 'deque'
        # Require `from collections import deque`
        """
        actions = deque()
        actions.append((0,1))
        record = set()

        while actions:
            step, position = actions.popleft()

            for move in moves:
                pos = position + move
                x, y = getIndex(pos)
                if (x, y) not in record:
                    pos = (pos if board[x][y] == -1 else board[x][y])
                    if pos == goal:
                        return step + 1
                    record.add((x, y))
                    actions.append((step + 1, pos))

        return -1
        """
