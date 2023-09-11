class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        output = []
        maximum = max(candies) - extraCandies
        for i in range(len(candies)):
            candies[i] = False if candies[i] < maximum else True

        return candies
