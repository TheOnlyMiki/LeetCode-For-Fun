class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # Option 3 - Time O(n^0.5), Space O(1)
        sqrt_n = int(sqrt(n))
        for i in range(1, sqrt_n+1):
            if n % i == 0:
                if k == 1:
                    return i
                k -= 1

        if sqrt_n * sqrt_n == n:
            sqrt_n -= 1

        for i in range(sqrt_n, 0, -1):
            if n % i == 0:
                if k == 1:
                    return n / i
                k -= 1

        return -1

        # Option 2 - Time O(n^0.5), Space O(n^0.5)
        """
        sqrt_n = int(sqrt(n))
        record = []
        for i in range(1, sqrt_n + 1):
            if n % i == 0:
                if k == 1:
                    return i
                record.append(i)
                k -= 1

        if sqrt_n == n // record[-1]:
            record.pop()

        return -1 if len(record)-k < 0 else n // record[len(record)-k]
        """

        # Option 1 - Time O(n)
        """
        for i in range(1, n//2+1):
            if n % i == 0:
                if k == 1:
                    return i
                k -= 1

        return n if k == 1 else -1
        """
