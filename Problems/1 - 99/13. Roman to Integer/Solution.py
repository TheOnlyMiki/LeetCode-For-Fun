class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman = {   'I' : 1,
                    'V' : 5,
                    'X' : 10,
                    'L' : 50,
                    'C' : 100,
                    'D' : 500,
                    'M' : 1000 }

        roman_special = {   "IV" : roman['I'] + roman['V'] - 4,
                            "IX" : roman['I'] + roman['X'] - 9,
                            "XL" : roman['X'] + roman['L'] - 40,
                            "XC" : roman['X'] + roman['C'] - 90,
                            "CD" : roman['C'] + roman['D'] - 400,
                            "CM" : roman['C'] + roman['M'] - 900  }

        num = 0
        i = 0
        refund = 0

        for special in roman_special:
            if special in s:
                refund += roman_special[special]

        for i, c in enumerate(s):
            num += roman[c]

        return num - refund
