class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if min(strs) == 0:
            return ""

        index = 200
        first_s_length = len(strs[0])

        for s in strs[1:]:
            match = 0

            for i, c in enumerate(s):
                if i == first_s_length:
                    break
                elif strs[0][i] == c:
                    match+=1
                else:
                    break

            index = min(match, index)

        return strs[0][:index]
