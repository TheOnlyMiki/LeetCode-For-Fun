# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Option 3
        output = 0
        record = [(root.left, True, 0), (root.right, False, 0)]

        while record:
            node, direction, count = record.pop()
            if node:
                if direction:
                    record += [(node.left, True, 0), (node.right, False, count+1)]
                else:
                    record += [(node.left, True, count+1), (node.right, False, 0)]
            else:
                if count > output:
                    output = count

        return output

        # Option 2
        """
        self.output = 0
        def dfs(node, direction, count):
            if not node:
                if count > self.output:
                    self.output = count
                return
            
            if direction:
                dfs(node.left, True, 0)
                dfs(node.right, False, count+1)
            else:
                dfs(node.left, True, count+1)
                dfs(node.right, False, 0)

        dfs(root.left, True, 0)
        dfs(root.right, False, 0)

        return self.output
        """
        
        # Option 1
        """
        def dfs(node, direction, count):
            if not node:
                return count
            
            if direction:
                return max(dfs(node.left, True, 0), dfs(node.right, False, count+1))
            else:
                return max(dfs(node.left, True, count+1),dfs(node.right, False, 0))

        return max(dfs(root.left, True, 0),dfs(root.right, False, 0))
        """
