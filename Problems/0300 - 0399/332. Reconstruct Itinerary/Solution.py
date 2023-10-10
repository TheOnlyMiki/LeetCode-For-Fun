class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # Option 2
        record = {}
        for start, end in tickets:
            if start in record:
                record[start].append(end)
            else:
                record[start] = [end]

        for key in record.keys():
            record[key].sort()
            record[key].reverse()
        
        def dfs(cameFrom):
            if cameFrom in record:
                while record[cameFrom]:
                    dfs(record[cameFrom].pop())

            self.output.append(cameFrom)

        self.output = []
        dfs("JFK")
        return self.output[::-1]

        # Option 1
        """
        total = len(tickets) + 1
        order = set()
        record = {}
        for start, end in tickets:
            order |= {start, end}
            if start in record:
                record[start][end] = record[start][end] + 1 if end in record[start] else 1
            else:
                record[start] = {end:1}

        order = sorted(order)
        
        def dfs(store, cameFrom):
            if len(store) == total:
                self.output = store[:]
                return True

            if cameFrom in record:
                for city in order:
                    if city in record[cameFrom] and record[cameFrom][city] != 0:
                        record[cameFrom][city] -= 1
                        if dfs(store + [city], city):
                            return True
                        record[cameFrom][city] += 1

            return False

        self.output = None
        dfs(["JFK"], "JFK")
        return self.output
        """
