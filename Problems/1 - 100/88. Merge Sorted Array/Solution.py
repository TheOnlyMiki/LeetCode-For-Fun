class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #Initial positive for nums1 and nums2
        x, y = 0, 0

        #Clone nums1 to the last 
        if n != 0: 
            if m != 0: nums1[m:] = nums1[:m]

            for i in range(m + n):
                if x == m:
                    nums1[i] = nums2[y]
                    y+=1
                elif y == n:
                    nums1[i] = nums1[m+x]
                    x+=1
                elif nums1[m+x] >= nums2[y]:
                    nums1[i] = nums2[y]
                    y+=1
                elif nums1[m+x] < nums2[y]:
                    nums1[i] = nums1[m+x]
                    x+=1
