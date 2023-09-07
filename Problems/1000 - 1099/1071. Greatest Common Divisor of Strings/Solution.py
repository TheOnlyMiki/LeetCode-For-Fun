class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        len1, len2 = len(str1), len(str2)
        num = min(len1, len2)
        devide1 = remain = devide2 = match = None
        
        while num != 0:
            devide1, remain = divmod(len1, num)
            if remain == 0:
                devide2, remain = divmod(len2, num)
                if remain == 0:
                    match = str2[:num]
                    if str1 == match * devide1 and str2 == match * devide2:
                        return match

            num -= 1

        return ""
