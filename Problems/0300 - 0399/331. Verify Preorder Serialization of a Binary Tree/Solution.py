class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nulls = 1
        for c in preorder.split(','):
            if nulls == 0:
                return False
            if c == '#':
                nulls -= 1
            else:
                nulls += 1

        return nulls == 0
