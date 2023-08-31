class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        number = {  0 : '',
                    1 : 'I',
                    5 : 'V',
                    10 : 'X',
                    50 : 'L',
                    100 : 'C',
                    500 : 'D',
                    1000 : 'M',
                    4 : "VI",
                    9 : "XI",
                    40 : "LX",
                    90 : "CX",
                    400 : "DC",
                    900 : "MC"  }

        roman = ""

        for i, v in enumerate(str(num)[::-1]):
            value = int(v)
            c_represend = 10**i
            over_5 = False

            if value > 5 and value != 9:
                over_5 = True
                value = value % 5

            represend = value * c_represend

            if represend in number:
                roman += number[represend]
            else:
                for _ in range(value):
                    roman += number[c_represend]

            if over_5:
                roman += number[5*c_represend]

        return roman[::-1]
