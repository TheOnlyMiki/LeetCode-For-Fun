class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        output = []
        length = len(candidates)

        def getNum(record, consum, index):
            if consum == target:
                output.append(record[:])
                return

            for i in xrange(index, length):
                consum += candidates[i]
                if consum <= target:
                    record.append(candidates[i])
                    getNum(record, consum, i)
                    record.pop()
                consum -= candidates[i]

        getNum([], 0, 0)

        return output
