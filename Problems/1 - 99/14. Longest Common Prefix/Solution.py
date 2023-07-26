class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Option 2
        first_s_length = len(strs[0])

        i = 0
        record = first_s_length
        range_remain_s = range(1, len(strs))

        while i < first_s_length:
            c = strs[0][i]

            for index in range_remain_s:
                if i == len(strs[index]) or strs[index][i] != c:
                    record = i
                    i = first_s_length
                    break

            i += 1

        return strs[0][:record]

        #Option 1
        """
        index = 200
        first_s_length = len(strs[0])

        for s in range(1,len(strs)):
            match = 0

            for i, c in enumerate(strs[s]):
                if i < first_s_length and strs[0][i] == c:
                    match+=1
                else:
                    break

            index = min(match, index)

        return strs[0][:index]
        """
