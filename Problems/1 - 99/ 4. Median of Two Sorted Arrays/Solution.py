class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length1 = len(nums1)
        length2 = len(nums2)

        if length1 < length2:
            return self.findMedianSortedArrays(nums2, nums1)

        length = length1 + length2
        length1 *= 2
        length2 *= 2
        
        left, right = 0, length2
        mid1 = mid2 = None
        left1 = left2 = right1 = right2 = None

        while left <= right:
            mid1 = (left + right) // 2
            mid2 = length - mid1
            #print(left, right)
            #print(mid1, mid2)

            left1 = -10000000 if mid2 == 0 else nums1[(mid2-1)/2]
            right1 = 10000000 if mid2 == length1 else nums1[mid2/2]
            left2 = -10000000 if mid1 == 0 else nums2[(mid1-1)/2]
            right2 = 10000000 if mid1 == length2 else nums2[mid1/2]
            #print(left1, left2, right1, right2)

            if left1 > right2:
                left = mid1 + 1
            elif left2 > right1:
                right = mid1 - 1
            else:
                return (max(left1, left2) + min(right1, right2)) / 2.0

        return -1
