class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        count = [1] * n
        lowest = min(ratings)
        low_index = ratings.index(lowest)

        for i in range(low_index + 1, n):
            if ratings[i] > ratings[i - 1]:
                count[i] = count[i - 1] + 1
            else:
                count[i] = count[i - 1] - 1

        for i in range(low_index - 1, -1 ,-1):
            if ratings[i] > ratings[i + 1]:
                count[i] = count[i + 1] + 1
            else:
                count[i] = count[i + 1] - 1

        return sum(count)
