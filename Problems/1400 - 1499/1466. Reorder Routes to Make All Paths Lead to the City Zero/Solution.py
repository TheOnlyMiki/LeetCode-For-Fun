class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        visit = [True] * n
        record = [[] for i in range(n)]
        for a, b in connections:
            record[a].append(b)
            record[b].append(-a)

        output = 0
        stack = [0]
        while stack:
            temp = []
            for i in stack:
                if visit[i]:
                    visit[i] = False
                    for b in record[i]:
                        if visit[abs(b)]:
                            temp.append(abs(b))
                            if b > 0:
                                output += 1

            stack = temp

        return output
