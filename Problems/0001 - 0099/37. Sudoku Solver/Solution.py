class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        area = { 
            (0,0) : set(), (0,1) : set(), (0,2) : set(), 
            (1,0) : set(), (1,1) : set(), (1,2) : set(), 
            (2,0) : set(), (2,1) : set(), (2,2) : set(), 
        }
        area_code = {0:0, 1:0, 2:0, 3:1, 4:1, 5:1, 6:2, 7:2, 8:2}

        horizontal = {}
        vertical = {}

        cols = range(9)
        for n in cols:
            horizontal[n] = set()
            vertical[n] = set()

        insertList = []
        for i in cols:
            for j in cols:
                if board[i][j] == '.':
                    insertList.append((i, j))
                else:
                    area[ (area_code[i], area_code[j]) ].add(board[i][j])
                    horizontal[i].add(board[i][j])
                    vertical[j].add(board[i][j])

        def solver():
            if not insertList:
                return True

            i, j = insertList.pop()

            for num in "123456789":
                # Check if the number is valid to insert to Sudoku
                if (num in horizontal[i] or num in vertical[j] or
                    num in area[ (area_code[i], area_code[j]) ]):
                    continue

                # Insert the valid number in to Sudoku and update the valid list
                board[i][j] = num
                area[ (area_code[i], area_code[j]) ].add(num)
                horizontal[i].add(num)
                vertical[j].add(num)

                if solver():
                    return True

                # Remove the number from Sudoku and valid list
                board[i][j] = '.'
                area[ (area_code[i], area_code[j]) ].remove(num)
                horizontal[i].remove(num)
                vertical[j].remove(num)

            insertList.append((i, j))
            
        solver()
