class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        devide = 2
        domain, remain = divmod(length, devide)
        i = temp = None

        while domain != 0:
            if remain == 0:
                temp = s[:domain]
                i = domain

                while i < length:
                    if temp != s[ i : i+domain ]:
                        break
                    i += domain

                if i == length:
                    return True

            devide += 1
            domain, remain = divmod(length, devide)

        return False
