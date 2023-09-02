class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Option 2 - Bit Operation
        output = 0
        if abs(divisor) == 1:
            output = dividend if divisor == 1 else -dividend
            limit = 2**31

            if output < -limit:
                return -limit
            if output >= limit:
                return limit-1

            return output
        
        x, y = abs(dividend), abs(divisor)
        for i in range(31, -1, -1):
            if (x >> i) - y >= 0:
                output += 1 << i
                x -= y << i

        return output if (dividend > 0) == (divisor > 0) else -output

        # Option 1 - Very Basic method, cannot pass
        """
        output = 0
        sign = 1
        limit = 2**31

        if divisor == 1:
            output = dividend
        elif divisor == -1:
            output = -dividend
        else:
            if dividend < 0:
                dividend = -dividend
                if divisor < 0:
                    divisor = -divisor
                else:
                    sign = -sign
            elif dividend > 0:
                if divisor < 0:
                    divisor, sign = -divisor, -sign
            
            while dividend >= divisor:
                dividend -= divisor
                output += sign

        if output < -limit:
            return -limit
        if output >= limit:
            return limit-1

        return output
        """
