class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        count = [1] * n
        
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                count[i] = count[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                count[i] = max(count[i], count[i+1] + 1)

        return sum(count)
