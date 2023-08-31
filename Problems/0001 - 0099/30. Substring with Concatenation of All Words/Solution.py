class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        word_len = len(words[0])
        subarray_len = len(words) * word_len

        count = {}
        for word in words:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

        output = []
        i = 0

        while i < len(s) - subarray_len + 1:
            temp_count = {}
            for index in range(i, i + subarray_len, word_len):
                subarray = s[ index : index + word_len ]
                if subarray in temp_count:
                    temp_count[subarray] += 1
                else:
                    temp_count[subarray] = 1

            if temp_count == count:
                output.append(i)

            i += 1

        return output
