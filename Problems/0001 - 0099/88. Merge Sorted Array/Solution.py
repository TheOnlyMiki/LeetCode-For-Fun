class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Option 2 - In place Method
        if n == 0:
            return

        if m == 0:
            nums1[:] = nums2[:]
            return
        
        #Initial positive for nums1 and nums2
        x, y, i = m-1, n-1, m+n-1
        while x != -1 and y != -1:
            if nums1[x] > nums2[y]:
                nums1[i] = nums1[x]
                x -= 1
            else:
                nums1[i] = nums2[y]
                y -= 1
            i -= 1

        if y != -1:
            nums1[:y+1] = nums2[:y+1]

        # Option 1 - Space O(m)
        """
        #Initial positive for nums1 and nums2
        x, y = 0, 0

        clone_nums1 = nums1[:]

        for i in range(m + n):
            if x == m:
                nums1[i] = nums2[y]
                y+=1
            elif y == n:
                nums1[i] = clone_nums1[x]
                x+=1
            elif clone_nums1[x] >= nums2[y]:
                nums1[i] = nums2[y]
                y+=1
            elif clone_nums1[x] < nums2[y]:
                nums1[i] = clone_nums1[x]
                x+=1
        """
