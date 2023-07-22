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
        x, y, length = 0, 0, m + n

        #Clone nums1
        clone_nums1 = nums1[:]

        # Forloop in O(m+n)
        for i in range(length):
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
            
        print(nums1)
