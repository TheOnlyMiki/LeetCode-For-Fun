# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def getResult(left, right):
            if left > right:
                return [None]

            nodes = []
            for mid in range(left, right+1):
                for leftNode in getResult(left, mid-1):
                    for rightNode in getResult(mid+1, right):
                        nodes.append(TreeNode(mid, leftNode, rightNode))

            return nodes

        return getResult(1, n)
