class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        length = len(word)

        m = len(board)
        n = len(board[0])
        cols = range(n)

        def checkWord(x, y, i):
            c = board[x][y]
            board[x][y] = None

            if i == length:
                return True

            for a, b in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_x, next_y = x+a, y+b
                if -1 < next_x < m and -1 < next_y < n and board[next_x][next_y] == word[i]:
                    if checkWord(next_x, next_y, i+1):
                        return True

            board[x][y] = c
            return False

        for x in range(m):
            for y in cols:
                if board[x][y] == word[0] and checkWord(x, y, 1):
                    return True

        return False
