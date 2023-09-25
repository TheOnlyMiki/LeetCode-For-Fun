class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        previou_1, previou_2 = cost[0], cost[1]
        for i in range(2, len(cost)):
            previou_1, previou_2 = previou_2, min(previou_1, previou_2) + cost[i]

        return min(previou_1, previou_2)
