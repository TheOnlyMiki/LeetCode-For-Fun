class Solution(object):
    def positiveCheck(self, num):
            if num > 0:
                return True
            return False

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        count = {}
        output = set()

        # Count the number of occurrences - O(n)
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        zero_exist = False
        if 0 in count:
            zero_exist = True
            if count[0] > 2:
                output.add((0,0,0))
            del count[0]

        record_count = count.keys() #List
        record_count_len = len(record_count)
            
        while record_count_len != 0:
            a = record_count[0]
            del record_count[0]
            record_count_len -= 1

            if zero_exist and -a in count:
                output.add(tuple(sorted([-a,0,a])))

            # a + b + c = 0 -> c = 0 - a - b
            for b in record_count:
                c = -a - b
                if c in count:
                    if a == b:
                        if count[a] > 1:
                            output.add(tuple(sorted([a,a,c])))
                    elif b == c:
                        if count[b] > 1:
                            output.add(tuple(sorted([a,b,b])))
                    elif a == c:
                        if count[a] > 1:
                            output.add(tuple(sorted([a,a,b])))
                    else:
                        output.add(tuple(sorted([a,b,c])))

        return output
