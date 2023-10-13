class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Option 4 - If we know the maximum for power of 3
        #return n > 0 and 3**19 % n == 0
        return n > 0 and 1162261467 % n == 0

        # Option 3 - BF, Devide by 3
        """
        if n < 1:
            return False

        while n != 1:
            n, temp = divmod(n, 3)
            if temp != 0:
                return False

        return True
        """

        # Option 2 - BF, Times 3 with global variable
        """
        global record
        try:
            return n in record
        except:
            record = {1}
            num = 1
            for _ in range(19):
                num *= 3
                record.add(num)

        return n in record
        """

        # Option 1 - BF, Times 3
        """
        num = 1
        while num < n:
            num *= 3

        return n == num
        """
