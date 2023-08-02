class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []
        num = num_2 = None

        for item in tokens:
            if item == '+':
                num = stack[-1]
                stack.pop()
                num_2 = stack[-1]
                stack.pop()
                stack.append(num_2 + num)

            elif item == '-':
                num = stack[-1]
                stack.pop()
                num_2 = stack[-1]
                stack.pop()
                stack.append(num_2 - num)

            elif item == '*':
                num = stack[-1]
                stack.pop()
                num_2 = stack[-1]
                stack.pop()
                stack.append(num_2 * num)

            elif item == '/':
                num = stack[-1]
                stack.pop()
                num_2 = stack[-1]
                stack.pop()
                stack.append(int(float(num_2) / num))

            else:
                stack.append(int(item))

        return stack[0]
