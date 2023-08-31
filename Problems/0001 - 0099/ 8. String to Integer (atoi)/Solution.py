class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Option 2
        output = 0
        symbol = 1
        represent = { 
            '0' : 0,
            '1' : 1,
            '2' : 2,
            '3' : 3,
            '4' : 4,
            '5' : 5,
            '6' : 6,
            '7' : 7,
            '8' : 8,
            '9' : 9
        }

        i = 0
        length = len(s)

        while i < length and s[i] == ' ':
            i += 1

        if i < length and s[i] == '-':
            symbol = -1
            i += 1
        elif i < length and s[i] == '+':
            i += 1

        while i < length and s[i] in represent:
            output = output*10 + represent[s[i]]
            i += 1

        output *= symbol
        board = 2**31

        return min(output, board-1) if output >= 0 else max(output, -board)

        # Option 1
        """
        output = 0
        symbol = True
        break_condition = True
        represent = { 
            '0' : 0,
            '1' : 1,
            '2' : 2,
            '3' : 3,
            '4' : 4,
            '5' : 5,
            '6' : 6,
            '7' : 7,
            '8' : 8,
            '9' : 9,
            '-' : 10,
            '+' : 11,
            ' ' : 12
         }

        for c in s:
            if c not in represent:
                break

            if break_condition:
                if represent[c] < 10:
                    output = output*10 + represent[c]
                elif c == ' ':
                    continue
                elif c == '-':
                    symbol = False

                break_condition = False
                del represent['-']
                del represent['+']
                del represent[' ']
                continue
            
            output = output*10 + represent[c]

        output = output if symbol else -output
        board = 2**31

        if output >= board:
            output = board-1
        elif output < -board:
            output = -board

        return output
        """
