class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # Option 2 - Fast
        self.record = []
        def getCombination(i, remain, k):
            if k == 0:
                if remain == 0:
                    self.output.append(self.record[:])
                return
            
            for num in range(i, 10):
                if remain - num < 0:
                    return
                
                self.record.append(num)
                getCombination(num+1, remain-num, k-1)
                self.record.pop()

        self.output = []
        getCombination(1, n, k)

        return self.output

        # Option 1 - Using less space, but time complexity were too bigger(so slowly)
        """
        represent = [1,2,3,4,5,6,7,8,9]
        record = set()
        visit = {1,2,3,4,5,6,7,8,9}

        def getCombination(remain, k):
            if k == 1:
                if remain in visit:
                    temp = record | {remain}
                    if temp not in self.output:
                        self.output.append(temp)
                    return
            else:
                for num in represent:
                    if num in visit and remain - num > 0:
                        visit.remove(num)
                        record.add(num)
                        getCombination(remain - num, k-1)
                        record.remove(num)
                        visit.add(num)

        self.output = []
        getCombination(n, k)

        return self.output
        """
