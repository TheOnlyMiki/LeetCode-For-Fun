class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        # Option 2 - Hash Table method
        first2record = {}
        for x1 in nums1:
            for x2 in nums2:
                if x1+x2 in first2record:
                    first2record[x1+x2] += 1
                else:
                    first2record[x1+x2] = 1

        count = 0
        for x1 in nums3:
            for x2 in nums4:
                if -x1-x2 in first2record:
                    count += first2record[-x1-x2]
        
        return count

        # Option 1 - BF method, Time O(n^4)
        """
        n = len(nums1)

        count = 0
        for x1 in nums1:
            for x2 in nums2:
                for x3 in nums3:
                    for x4 in nums4:
                        if x1+x2+x3+x4 == 0:
                            count += 1
        
        return count
        """
