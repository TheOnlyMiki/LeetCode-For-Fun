class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n = len(gas)

        for i in range(n+1):
            i = i % n
            start_gas = 0
            reachable = 0
            for i_2 in range(n+1):
                i_2 = (i + i_2) % n
                start_gas += gas[i_2]
                if start_gas < cost[i_2]:
                    break
                else:
                    start_gas -= cost[i_2]
                    reachable+=1
            
            if reachable == n+1:
                return i

        return -1
