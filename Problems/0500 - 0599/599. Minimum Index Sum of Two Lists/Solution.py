class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        indexs = { word:i for i, word in enumerate(list1) }
        minimum, output = len(list1)+len(list2), []
        for i, word in enumerate(list2):
            if word in indexs:
                if minimum == indexs[word] + i:
                    output.append(word)
                elif minimum > indexs[word] + i:
                    minimum, output = indexs[word] + i, [word]

        return output
