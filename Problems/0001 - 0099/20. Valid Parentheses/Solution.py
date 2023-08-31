class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        represent = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        stack = []

        try:
            for c in s:
                if c in represent:
                    stack.append(represent[c])
                elif stack[-1] == c:
                    stack.pop()
                else:
                    return
        except:
            return False

        return len(stack) == 0
