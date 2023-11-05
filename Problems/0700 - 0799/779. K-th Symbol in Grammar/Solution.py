class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # Option 2
        def getOutput(n, k):
            if n == 1:
                return 0
            if k & 1 == 0:
                return 1 if getOutput(n-1, k>>1) == 0 else 0
            else:
                return 0 if getOutput(n-1, (k+1)>>1) == 0 else 1

        return getOutput(n, k)

        # Option 1 - BF method, cannot pass
        """
        length = 2
        current = "0110"
        while len(current) < k:
            cut, length = length, len(current)
            current += current[cut:] + current[:cut]
        
        return int(current[k-1])
        """
