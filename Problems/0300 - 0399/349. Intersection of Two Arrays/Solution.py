class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Option 2 - Sorting and Binary Search
        nums1.sort()
        nums2.sort()
        output = set()
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                output.add(nums1[i])
                i, j = i+1, j+1

        return list(output)

        # Option 1 - Insert Set
        return list(set(nums1) & set(nums2))
