# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Option 2
        self.max_sum = -1001

        def findMaxPathSum2(root):
            if not root:
                return 0

            left_max = max(findMaxPathSum2(root.left), 0)
            right_max = max(findMaxPathSum2(root.right), 0)

            self.max_sum = max(self.max_sum, root.val + left_max + right_max)

            return root.val + max(left_max, right_max)

        findMaxPathSum2(root)
        return self.max_sum
         
        # Option 1 - This is not corret, this is for maximum whole path
        """
        def findMaxPathSum(root):
            if root.left and root.right:
                left_max, pre_left_max_sum = findMaxPathSum(root.left)
                right_max, pre_right_max_sum = findMaxPathSum(root.right)

                connect_max_sum = max(left_max + root.val, right_max + root.val, root.val, left_max + right_max + root.val)
                suboptimal_max_sum = max(left_max, right_max, pre_left_max_sum, pre_right_max_sum, connect_max_sum)
                print("LR:", root.val, connect_max_sum, suboptimal_max_sum)
                return connect_max_sum, suboptimal_max_sum
            elif root.left:
                left_max, pre_max_sum = findMaxPathSum(root.left)
                connect_max_sum = max(left_max + root.val, root.val)
                suboptimal_max_sum = max(left_max, pre_max_sum, connect_max_sum)
                print("L:", root.val, connect_max_sum, suboptimal_max_sum)
                return connect_max_sum, suboptimal_max_sum
            elif root.right:
                right_max, pre_max_sum = findMaxPathSum(root.right)
                connect_max_sum = max(right_max + root.val, root.val)
                suboptimal_max_sum = max(right_max, pre_max_sum, connect_max_sum)
                print("R:", root.val, connect_max_sum, suboptimal_max_sum)
                return connect_max_sum, suboptimal_max_sum
            else:
                print("E:", root.val)
                return root.val, root.val

        return max(findMaxPathSum(root))
        """
