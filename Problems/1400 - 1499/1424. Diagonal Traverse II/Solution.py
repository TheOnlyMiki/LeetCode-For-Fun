class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # Option 3 - Queue
        last_row = len(nums)-1
        queue = deque([(0, 0)])
        output = []

        while queue:
            i, j = queue.popleft()
            output.append(nums[i][j])
            if j == 0 and i != last_row:
                queue.append((i+1, j))
            if j != len(nums[i])-1:
                queue.append((i, j+1))

        return output

        # Option 2 - Hash Table
        """
        record = {}
        for i in range(len(nums)-1, -1, -1):
            for j in range(len(nums[i])-1, -1, -1):
                if i+j in record:
                    record[i+j].append(nums[i][j])
                else:
                    record[i+j] = [nums[i][j]]
            
            '''
            for j in range(i+len(nums[i])-1, i-1, -1):
                if j in record:
                    record[j].append(nums[i][j-i])
                else:
                    record[j] = [nums[i][j-i]]
            '''

            '''
            for j in range(i+len(nums[i])-1, i-1, -1):
                record[j] = record[j] + [nums[i][j-i]] if j in record else [nums[i][j-i]]
            '''
        
        '''
        output = []
        for i in range(len(record)):
            output += record.pop(i)

        return output
        '''
        return [j for i in record for j in record[i]]
        """

        # Option 1 - BF, slow, cannot pass
        """
        row, loop, limit = len(nums), len(nums) + len(nums[0]), 1e5

        def read(i, j):
            while j < limit:
                if j < len(nums[i]):
                    output.append(nums[i][j])
                if i == 0:
                    return
                i, j = i-1, j+1

        i, output = 0, []
        while i < loop:
            if i < row:
                if row + len(nums[i]) > loop:
                    loop = row + len(nums[i]) 
                read(i, 0)
            else:
                read(row-1, i-row+1)
            i += 1

        return output
        """
