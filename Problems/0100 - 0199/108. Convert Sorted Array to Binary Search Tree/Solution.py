# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        def sortedListToBST(left, right):
            if left < right:
                mid = (right + left) // 2
                current = TreeNode(nums[mid])
                current.left = sortedListToBST(left, mid)
                current.right = sortedListToBST(mid+1, right)
                return current

            return None

        head = sortedListToBST(0, len(nums))

        return head
