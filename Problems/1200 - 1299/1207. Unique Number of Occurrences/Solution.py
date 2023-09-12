class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # Option 2
        """
        visit = set()
        temp = None
        for num in set(arr):
            temp = arr.count(num)
            if temp in visit:
                return False
            visit.add(temp)

        return True
        """

        # Option 1
        count = {}
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        return len(count) == len(set(count.values()))
