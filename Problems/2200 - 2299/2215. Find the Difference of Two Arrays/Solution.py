class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        # Option 2
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        common_set = nums1_set & nums2_set
        return [list(nums1_set - common_set), list(nums2_set - common_set)]

        # Option 1
        """
        nums1_set = set(nums1)
        nums2_set = set()
        common_set = set()
        for num in nums2:
            if num in nums1_set:
                common_set.add(num)
            else:
                nums2_set.add(num)

        return [list(nums1_set - common_set), list(nums2_set)]
        """
