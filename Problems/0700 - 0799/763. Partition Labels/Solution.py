class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

        i = 0
        visit = set()
        output = []
        for c in s:
            visit.add(c)
            count[c] -= 1
            i += 1

            if count[c] == 0:
                visit.remove(c)
            if len(visit) == 0:
                output.append(i)
                i = 0

        return output
