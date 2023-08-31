class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        record = { stone:set() for stone in stones }
        record[stones[0]] = {0}
        temp = stone = None

        for i in range(len(stones)-1):
            stone = stones[i]
            for k in record.pop(stone):
                temp = stone + k
                if temp+1 in record:
                    record[temp+1].add(k+1)
                if temp in record:
                    record[temp].add(k)
                if temp-1 in record:
                    record[temp-1].add(k-1)

        return True if record[stones[-1]] else False
