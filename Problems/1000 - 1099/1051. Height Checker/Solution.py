class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Option 1 - Hash Table method, Time O(n)
        record = {}
        for n in heights:
            record[n] = record[n]+1 if n in record else 1

        count, num = 0, 1
        for n in heights:
            while num not in record:
                num += 1

            if n != num:
                count += 1

            record[num] -= 1
            if record[num] == 0:
                num += 1

        return count

        # Option 1 - Sorting method
        """
        correct = sorted(heights)
        count = 0
        for p1, p2 in zip(heights, correct):
            if p1 != p2:
                count += 1

        return count
        """
