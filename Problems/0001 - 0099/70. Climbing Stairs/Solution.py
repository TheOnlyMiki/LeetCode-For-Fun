class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = {0:0, 1:1, 2:2, 3:3}

        def calculator(n):
            if n in count:
                return count[n]

            count[n] = calculator(n-1) + calculator(n-2)
            return count[n]

        return calculator(n)
        
