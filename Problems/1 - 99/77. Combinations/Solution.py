class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        output = []
        def getNext(start, record):
            if len(record) == k:
                output.append(record[:])
                return

            for num in range(start, n+1):
                record.append(num)
                getNext(num+1, record)
                record.pop()

        getNext(1, [])
        return output
