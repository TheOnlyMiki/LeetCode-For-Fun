class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        record = set(arr)
        for n in record:
            if n*2 in record:
                if n*2 == n and arr.count(n) == 1:
                    continue
                return True

        return False
