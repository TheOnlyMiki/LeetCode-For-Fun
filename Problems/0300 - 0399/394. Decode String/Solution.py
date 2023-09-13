class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        represent_nums = {c for c in "0123456789"}
        time = word = None

        for c in s:
            if c == ']':
                time, word = "", ""
                while stack[-1] != '[':
                    word = stack.pop() + word

                stack.pop()
                while stack and stack[-1] in represent_nums:
                    time = stack.pop() + time

                stack.append(int(time) * word)
            else:
                stack.append(c)

        return ''.join(stack)
