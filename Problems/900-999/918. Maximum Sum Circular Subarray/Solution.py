class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Option 2 - Math method
        consum = consum2 = 0
        record, record2 = -300000, 300000
        for num in nums:
            consum += num
            consum2 += num

            record = max(record, consum)
            record2 = min(record2, consum2)

            if consum < 0:
                consum = 0
            if consum2 > 0:
                consum2 = 0

        sum_nums = sum(nums)
        if sum_nums - record2 == 0:
            return record

        return max(record, sum_nums - record2)

        # Option 1 - queue method
        """
        consum = 0
        record = -300000
        length = len(nums)
        record_sum = []
        for num in nums+nums:
            consum += num
            record_sum.append(consum)

        queue = [0]

        for i in xrange(1, 2*length):
            while queue and i - queue[0] > length:
                del queue[0]

            record = max(record, record_sum[i] - record_sum[queue[0]])

            while queue and record_sum[queue[-1]] > record_sum[i]:
                queue.pop()

            queue.append(i)

        return record
        """
