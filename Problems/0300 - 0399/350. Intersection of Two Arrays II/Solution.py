class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Option 2 - Hash Table
        """
        record = {}
        for num in nums1:
            record[num] = record[num] + 1 if num in record else 1

        output = []
        for num in nums2:
            if num in record and record[num] != 0:
                output.append(num)
                record[num] -= 1

        return output
        """

        # Option 1 - Sorting and Binary Search
        nums1.sort()
        nums2.sort()
        x, y = len(nums1), len(nums2)
        output = []
        i, j = 0, 0
        while i < x and j < y:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                output.append(nums1[i])
                i, j = i+1, j+1

        return output
