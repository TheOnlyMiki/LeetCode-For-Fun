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
