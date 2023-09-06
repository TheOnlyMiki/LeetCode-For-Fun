class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Option 2
        previou_2, previou_1 = 0, 1
        for i in range(1, n):
            previou_2, previou_1 = previou_1, previou_2+previou_1

        return previou_1 if n > 1 else n

        # Option 1
        """
        record = {0:0, 1:1, 2:1}

        def getFib(num):
            if num in record:
                return record[num]

            record[num] = getFib(num-1) + getFib(num-2)
            return record[num]

        return getFib(n)
        """
