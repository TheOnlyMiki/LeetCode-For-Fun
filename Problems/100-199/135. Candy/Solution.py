class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        #count = [1] * n
        count1 = {}

        for i, value in enumerate(ratings):
            if value in count1:
                count1[value].append(i)
            else:
                count1[value] = [i]

        lowest = min(count1.keys())
        low_list = count1[lowest]
        count_candy = []

        for low_index in low_list:
            count = [1] * n
            for i in range(low_index + 1, n):
                if ratings[i] > ratings[i - 1]:
                    count[i] = count[i - 1] + 1
                else:
                    count[i] = count[i - 1] - 1

            for i in range(low_index - 1, -1 ,-1):
                if ratings[i] > ratings[i + 1]:
                    count[i] = count[i + 1] + 1
                else:
                    count[i] = count[i + 1] - 1

            count_candy.append(sum(count))

        return min(count_candy)
