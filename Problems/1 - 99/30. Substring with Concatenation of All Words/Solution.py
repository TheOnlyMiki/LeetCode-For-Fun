class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        words_len = len(words)
        word_len = len(words[0])
        subarray_len = words_len * word_len

        if len(s) < subarray_len:
            return []

        count = {}
        for word in words:
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

        output = []
        i, i_2 = 0, subarray_len-1
        current_subarray = {}

        while i_2 < len(s):
            for index in range(i, i + subarray_len, word_len):
                subarray = s[ index : index + word_len ]
                if subarray in current_subarray:
                    current_subarray[subarray] += 1
                else:
                    current_subarray[subarray] = 1

            match = 0
            for word, value in count.items():
                if word in current_subarray and current_subarray[word] == value:
                    match += 1
                else:
                    break

            if match == len(count):
                output.append(i)

            current_subarray.clear()
            i += 1
            i_2 += 1

        return output
