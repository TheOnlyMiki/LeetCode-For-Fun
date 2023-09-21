class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        # Option 2
        citys = range(len(isConnected[0]))
        count = 0
        record = set()

        def connectCity(city):
            record.add(city)
            for i in citys:
                if i not in record and isConnected[city][i] == 1:
                    connectCity(i)
        
        for i in range(len(isConnected)):
            if i not in record:
                count += 1
                connectCity(i)

        return count

        # Option 1
        """
        n = range(len(isConnected))
        record = {i:{i} for i in n}

        for citys in isConnected:
            temp = set()
            for i in n:
                if citys[i] == 1:
                    temp |= record[i]
            for i in temp:
                record[i] = temp
        
        count = 0
        for i in n:
            if i in record:
                count += 1
                for city in record.pop(i):
                    record.pop(city, None)

        return count
        """
