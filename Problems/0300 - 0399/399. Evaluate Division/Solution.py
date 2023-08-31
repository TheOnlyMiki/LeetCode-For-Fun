class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # Option 2
        record = {}
        connect = {}
        visit = set()

        def updateConnect(symbol1, symbol2):
            if symbol1 not in connect:
                connect[symbol1] = {symbol1}
            if symbol2 not in connect:
                connect[symbol2] = {symbol2}

            temp = connect[symbol1] | connect[symbol2]
            for s in temp:
                connect[s] = temp

        def getResult(sym1, sym2, value):
            if sym2 in record[sym1]:
                return value * record[sym1][sym2]

            visit.add(sym1)
            for sym in record[sym1]:
                if sym not in visit:
                    temp = getResult(sym, sym2, value * record[sym1][sym])
                    if temp:
                        return temp
                
            visit.remove(sym1)
            return None

        com1 = com2 = None
        for i, (x1, x2) in enumerate(equations):
            if x1 not in record:
                record[x1] = {}
            if x2 not in record:
                record[x2] = {}

            record[x1][x2] = values[i]
            record[x2][x1] = 1/values[i]
            updateConnect(x1, x2)

        output = []
        for i, (x1, x2) in enumerate(queries):
            if x1 in record and x2 in record and x1 in connect[x2]:
                if x1 == x2:
                    output.append(1.0)
                else:
                    visit.clear()
                    output.append(getResult(x1, x2, 1))
            else:
                output.append(-1.0)

        return output

        # Option 1 - Can't pass, because this not accury
        """
        equations = sorted(zip(equations, values), key=(lambda x:x[0][1]))

        record = {}
        connect = {}
        product = 3000

        def updateConnect(symbol, symbol2):
            if symbol not in connect:
                temp = {symbol} | connect[symbol2]
            elif symbol2 not in connect:
                temp = {symbol2} | connect[symbol]
            else:
                temp = connect[symbol] | connect[symbol2]

            for s in temp:
                connect[s] = temp

        for i, (x,y) in enumerate(equations):
            symbol, symbol2 = (x[0] in record), (x[1] in record)
            if not symbol and not symbol2:
                record[x[1]] = product
                record[x[0]] = y * product
                connect[x[0]] = connect[x[1]] = set([x[1], x[0]])
            elif symbol:
                record[x[1]] = record[x[0]] / y
                updateConnect(x[0], x[1])
            elif symbol2:
                record[x[0]] = record[x[1]] * y
                updateConnect(x[0], x[1])
            else:
                updateConnect(x[0], x[1])

        output = []
                
        for i, x in enumerate(queries):
            if x[0] not in record or x[1] not in record or x[0] not in connect[x[1]]:
                output.append(-1.0)
            else:
                output.append(record[x[0]] / record[x[1]])

        return output
        """
