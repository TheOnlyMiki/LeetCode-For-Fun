class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        represend = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }

        digits = list(digits)

        output = ['']
        temp = None
        for digit in digits:
            temp = []
            for item in output:
                temp.extend([ item + c for c in represend[digit] ])
            output = temp

        return ( output if output[0] != '' else [] )
