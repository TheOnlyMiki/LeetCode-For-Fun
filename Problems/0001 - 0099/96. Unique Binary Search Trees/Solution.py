class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Option 2 - Dynamic Programming
        record = [0] * (n+1)
        record[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                record[i] += record[j] * record[i-j-1]

        return record[n]

        # Option 1 - DFS
        """
        record = {0:1}

        def dfs(n):
            if n in record:
                return record[n]

            total = 0
            for i in range(n):
                total += dfs(i) * dfs(n-i-1)

            record[n] = total
            return total 

        return dfs(n)
        """
