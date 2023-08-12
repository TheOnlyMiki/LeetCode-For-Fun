class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        self.output = 2*n
        cols = range(n)
        invalidCols = [False]*n
        invalidAngle, invalidAntiAngle = [False]*self.output, [False]*self.output

        def getNumQueen(row):
            if row == n:
                self.output += 1
                return

            for col in cols:
                angle, antiAngle = col - row + n, col + row
                if invalidCols[col] or invalidAngle[angle] or invalidAntiAngle[antiAngle]:
                    continue
                invalidCols[col] = invalidAngle[angle] = invalidAntiAngle[antiAngle] = True
                getNumQueen(row+1)
                invalidCols[col] = invalidAngle[angle] = invalidAntiAngle[antiAngle] = False

        self.output = 0
        getNumQueen(0)

        return self.output
