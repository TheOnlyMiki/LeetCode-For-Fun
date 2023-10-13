# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        # Option 2 - Same as Option 1
        """
        def findIndexIncrease(left, right):
            if left <= right:
                mid = (left + right) >> 1
                current = mountain_arr.get(mid)

                if current > target:
                    return findIndexIncrease(left, mid-1)
                elif current < target:
                    return findIndexIncrease(mid+1, right)
                else:
                    return mid

            return -1

        def findIndexDecrease(left, right):
            if left <= right:
                mid = (left + right) >> 1
                current = mountain_arr.get(mid)

                if current > target:
                    return findIndexDecrease(mid+1, right)
                elif current < target:
                    return findIndexDecrease(left, mid-1)
                else:
                    return mid

            return -1

        l, r = 0, mountain_arr.length()-1
        while l < r:
            mid = (l + r) >> 1
            if mountain_arr.get(mid) < mountain_arr.get(mid+1):
                l = mid+1
            else:
                r = mid

        output = findIndexIncrease(0, l)
        return output if output != -1 else findIndexDecrease(l+1, mountain_arr.length()-1)
        """

        # Option 1 - Find the higher point in the array, then find the index from two part
        # Left part if increase order, right part is decrease order
        l, r = 0, mountain_arr.length()-1
        while l < r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid+1):
                l = mid+1
            else:
                r = mid

        left, right = 0, l
        while left <= right:
            mid = (left + right) // 2
            current = mountain_arr.get(mid)

            if current > target:
                right = mid-1
            elif current < target:
                left = mid+1
            else:
                return mid

        left, right = l+1, mountain_arr.length()-1
        while left <= right:
            mid = (left + right) // 2
            current = mountain_arr.get(mid)

            if current > target:
                left = mid+1
            elif current < target:
                right = mid-1
            else:
                return mid

        return -1
