class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Option 2
        ascii_0 = ord('0')
        direction = 1
        stack = [1]
        consum = 0
        digits = 0

        for i in s:
            if i.isdigit():
                digits = digits * 10 + ord(i) - ascii_0
            elif i == '(':
                stack.append(direction)
            elif i == ')':
                stack.pop()
            elif i != ' ':
                consum += direction * digits
                direction = (-1 if i == '-' else 1) * stack[-1]
                digits = 0

        return consum + direction * digits

        # Option 1 - Poor solution
        """
        stack = ['(']
        temp_num = ""
        num = num_2 = None

        for item in s + ')':
            # Handle dights 1234567890
            if item.isdigit():
                temp_num += item
            # Handle '('
            elif item == '(':
                stack.append(item)
            # Handle '+' '-' ')'
            elif item != ' ':
                # If the previou number exist, then push into stack
                if temp_num:
                    stack.append(temp_num)
                
                temp_num = ""
                
                # Handle ')'
                if item == ')':
                    num = num_2 = 0
                    last = None
                    
                    while stack[-1] != '(':
                        if stack[-1] == '+':
                            num_2 += num
                        elif stack[-1] == '-':
                            num_2 -= num
                        else:
                            num = int(stack[-1])
                        last = stack[-1]
                        stack.pop()
                    
                    stack.pop()
                    if last == '-' or last == '+':
                        stack.append(str(num_2))
                    else:
                        stack.append(str(num_2 + num))
                # Handle '+' or '-'
                else:
                    stack.append(item)

        return int(stack[0])
        """
