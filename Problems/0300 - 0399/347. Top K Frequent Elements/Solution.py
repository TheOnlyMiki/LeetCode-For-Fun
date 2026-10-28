class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        record = {}
        for num in nums:
            if num in record:
                record[num] += 1
            else:
                record[num] = 1

        record = sorted(record.items(), key=(lambda x:x[1]))

        output = []
        for _ in range(k):
            output.append(record.pop()[0])

        return output

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Method 1 - dict + sorted
        '''
        record = {}
        for n in nums:
            record[n] = record.get(n, 0) + 1

        count = []
        for n, x in record.items():
            count.append([x, n])

        count = sorted(count, reverse=True)

        return [ count[i][1] for i in range(k) ]'''
        # time complexity O(nlogn), space complexity O(n)

        # Method 2 - bucket
        record = {}
        for n in nums:
            record[n] = record.get(n, 0) + 1

        '''count = [ [] for _ in range(len(nums)+1)] 
        for n, x in record.items():
            count[x].append(n)

        output = []
        for n in reversed(count):
            for x in n:
                output.append(x)
                if len(output) == k:
                    break'''

        count = [0] * (len(nums) + 1)
        for n, x in record.items():
            if count[x] == 0:
                count[x] = [n]
            else:
                count[x].append(n)

        output = []
        for n in count[::-1]:
            if n != 0:
                output += n
            if len(output) >= k:
                break

        return output
        # time complexity O(n), space complexity O(n)
