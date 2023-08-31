class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        count = {}

        for word in strs:
            temp = "".join(sorted(word))
            if temp in count:
                count[temp].append(word)
            else:
                count[temp] = [word]

        return count.values()
