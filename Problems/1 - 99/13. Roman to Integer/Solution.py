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

        roman_special = {   "IV" : 2,
                            "IX" : 2,
                            "XL" : 20,
                            "XC" : 20,
                            "CD" : 200,
                            "CM" : 200  }

        # Pso code
        """
        roman_special = {   "IV" : roman['I'] + roman['V'] - 4,     #1+5-4=2
                            "IX" : roman['I'] + roman['X'] - 9,     #1+10-9=2
                            "XL" : roman['X'] + roman['L'] - 40,    #10+50-40=20
                            "XC" : roman['X'] + roman['C'] - 90,    #10+100-90=20
                            "CD" : roman['C'] + roman['D'] - 400,   #100+500-400=200
                            "CM" : roman['C'] + roman['M'] - 900  } #100+1000-900=200
        """

        num = 0

        for special in roman_special:
            if special in s:
                num -= roman_special[special]

        for c in s:
            num += roman[c]

        return num
