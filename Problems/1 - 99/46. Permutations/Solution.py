class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        visit = set()
        output = []

        def getNum(record):
            if length == len(record):
                output.append(record[:])
                return

            for item in nums:
                if item not in visit:
                    visit.add(item)
                    record.append(item)
                    getNum(record)
                    record.pop()
                    visit.remove(item)

        getNum([])
        return output
