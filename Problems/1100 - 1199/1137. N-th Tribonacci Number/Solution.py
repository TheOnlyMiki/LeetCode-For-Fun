class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        previou_0, previou_1, previou_2 = 0, 1, 1
        for _ in range(n-2):
            previou_0, previou_1, previou_2 = previou_1, previou_2, previou_0 + previou_1 + previou_2

        return 0 if n == 0 else previou_2
