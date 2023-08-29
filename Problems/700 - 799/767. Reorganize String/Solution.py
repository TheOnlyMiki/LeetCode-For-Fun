import heapq
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        length = len(s)
        record = []
        temp = c = nums = None
        for c in "abcdefghijklmnopqrstuvwxyz":
            temp = s.count(c)
            if temp > 0:
                heapq.heappush(record, [-temp, c])

        if length + record[0][0] < -(record[0][0]+1):
            return ""

        temp = 0
        while record[0][0] != 0:
            s[temp] = record[0][1]
            temp += 2
            record[0][0] += 1
        
        for i in range(1, len(record)):
            nums, c = record[i]
            while nums != 0:
                if temp >= length:
                    temp = 1

                s[temp] = c
                temp += 2
                nums += 1

        return ''.join(s)
