class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        # Option 2
        record1, record2 = sorted(set(word1)), sorted(set(word2))
        if record1 != record2:
            return False

        count1, count2 = [], []
        for i in range(len(record1)):
            count1.append(word1.count(record1[i]))
            count2.append(word2.count(record2[i]))

        return sorted(count1) == sorted(count2)

        # Option 1
        """
        if len(word1) != len(word2):
            return False

        count1, count2 = {}, {}
        for i in range(len(word1)):
            if word1[i] in count1:
                count1[word1[i]] += 1
            else:
                count1[word1[i]] = 1

            if word2[i] in count2:
                count2[word2[i]] += 1
            else:
                count2[word2[i]] = 1

        if len(count1) != len(count2) or sum(ord(x) for x in count1.keys()) != sum(ord(x) for x in count2.keys()):
            return False

        return sorted(count1.values()) == sorted(count2.values())
        """
