class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Option 2 - DFS
        i, temp, length = 2, 4, n+1
        prefect = {1}
        while temp < length:
            prefect.add(temp)
            i, temp = i+1, (i+1)**2

        def dfs(num, count):
            if count == 1:
                return num in prefect

            for n in prefect:
                if dfs(num-n, count-1):
                    return True
                
            return False

        for i in range(1, length):
            if dfs(n, i):
                return i

        return -1

        # Option 1 - Dynamic Programming method
        """
        i, temp, length = 2, 4, n+1
        prefect = []
        while temp < length:
            prefect.append(temp)
            i, temp = i+1, (i+1)**2

        # 0 - 10
        record = [0,1,2,3,1,2,3,4,2,1,2]
        for num in range(11, length):
            minimum = num - record[num-1]
            for square in prefect:
                if minimum == 0 or square > num:
                    break
                if minimum > record[num - square]:
                    minimum = record[num - square]

            record.append(minimum+1)
        
        return record[n]
        """
