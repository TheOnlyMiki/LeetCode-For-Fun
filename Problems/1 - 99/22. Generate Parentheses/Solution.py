class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output = []
        condition = 2*n
        self.valid = 0
            
        def getNum(record):
            if len(record) == condition:
                if self.valid == 0:
                    output.append(record)
                return

            # Opreation '('
            if self.valid != n:
                self.valid += 1
                getNum(record + '(')
                self.valid -= 1
            
            # Opreation '}'
            if self.valid != 0:
                self.valid -= 1
                getNum(record + ')')
                self.valid += 1

        getNum("")

        return output
