class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        devide = (n, n)
        i = 32
        output = 0
        while devide[0] != 0:
            devide = divmod(devide[0], 2)
            i -= 1
            if devide[1] == 1:
                output += 2**i

        return output
