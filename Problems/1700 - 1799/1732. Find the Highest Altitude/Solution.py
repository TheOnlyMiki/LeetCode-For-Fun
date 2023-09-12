class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        output = count = 0
        for num in gain:
            count += num
            if count > output:
                output = count

        return output
