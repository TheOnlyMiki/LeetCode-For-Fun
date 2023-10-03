class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        size = len(p)
        if size > len(s):
            return []

        def checkAllZero():
            for num in count.values():
                if num != 0:
                    return False

            return True

        total = 0
        count = {}
        for c in p:
            total += 1
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

        for c in s[:size-1]:
            if c in count:
                total -= 1
                count[c] -= 1

        output = []
        for i in range(size-1, len(s)):
            if s[i] in count:
                total -= 1
                count[s[i]] -= 1

            if total == 0:
                if checkAllZero():
                    output.append(i - size + 1)

            if s[i - size + 1] in count:
                total += 1
                count[s[i - size + 1]] += 1

        return output
