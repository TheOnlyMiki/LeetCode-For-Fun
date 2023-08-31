class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m, n = len(a), len(b)
        max_length = max(m, n)
        # key: a[i], b[i], carry ==> result, next carry
        represent = {
            "000" : "00",
            "001" : "10",
            "010" : "10",
            "011" : "01",
            "100" : "10",
            "101" : "01",
            "110" : "01",
            "111" : "11"
        }
        carry = "0"
        output = ""
        i = 0
        temp = None
        
        while i < max_length or carry == '1':
            temp = represent[ (a[-i-1] if i < m else '0') + (b[-i-1] if i < n else '0') + carry ]
            output += temp[0]
            carry = temp[1]
            i += 1
                
        return output[::-1]
