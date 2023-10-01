class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        previou = None
        output = [[1]]
        for i in range(1, numRows):
            output.append([1])
            for index in range(i-1):
                output[i].append(previou[index] + previou[index+1])
            output[i].append(1)
            previou = output[i]
            
        return output
