class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Option 2 - BF with Math
        record = [1] * n
        record[4 : n : 2] = [0] * ((n - 1 - 4) // 2 + 1)

        last_index, num, num_pow_2 = n-1, 3, 9
        while num_pow_2 < n:
            if record[num]:
                record[num_pow_2 : n : num] = [0] * ((last_index - num_pow_2) // num + 1)

            num, num_pow_2 = num+2, (num+2)**2

        return sum(record) - 2 if n > 2 else 0

        # Option 1 - BF
        """
        record = [1] * n
        for num in range(2, n):
            if record[num]:
                record[num*num : n : num] = [0] * len(record[num*num : n : num])

        return sum(record) - 2 if n > 2 else 0
        """
