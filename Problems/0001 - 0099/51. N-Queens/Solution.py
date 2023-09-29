class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        cols = range(n)
        invalidCols = [False] * n
        invalidAngle, invalidAntiAngle = [False]*(2*n), [False]*(2*n)

        def getQueen(row, store):
            if row == n:
                self.output.append(store[:])
                return

            for col in cols:
                angle, antiAngle = col - row + n, col + row
                if invalidCols[col] or invalidAngle[angle] or invalidAntiAngle[antiAngle]:
                    continue
                invalidCols[col] = invalidAngle[angle] = invalidAntiAngle[antiAngle] = True
                getQueen(row+1, store + ['.'*col + 'Q' + '.'*(n-col-1)])
                invalidCols[col] = invalidAngle[angle] = invalidAntiAngle[antiAngle] = False

        self.output = []
        getQueen(0, [])

        return self.output
