# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Option 3
        self.maxValue = 2**31
        self.minValue = -(self.maxValue+1)

        def checkBST(root, minValue, maxValue):
            if not root:
                return True
            if not minValue < root.val < maxValue:
                return False
            return checkBST(root.left, minValue, root.val) and checkBST(root.right, root.val, maxValue)

        return checkBST(root, self.minValue, self.maxValue)

        # Option 2 - Slow
        """
        self.maxValue = 2**31
        self.minValue = -self.maxValue

        def findMaxValue(root):
            if not root:
                return self.minValue
            
            value = max(findMaxValue(root.left), findMaxValue(root.right))
            return max(value, root.val)

        def findMinValue(root):
            if not root:
                return self.maxValue

            value = min(findMinValue(root.left), findMinValue(root.right))
            return min(value, root.val)

        def checkValid(root):
            if not root:
                return True

            if root.left and findMaxValue(root.left) >= root.val:
                return False
            if root.right and findMinValue(root.right) <= root.val:
                return False
            if not checkValid(root.left) or not checkValid(root.right):
                return False

            return True

        return checkValid(root)
        """

        # Option 1 - Too Slow
        # Build a BST, then compare it was the same as original tree
        """
        # fromLeft if True means from left node of parent
        def BST(value, root, parent, fromLeft=True):
            if not root:
                if fromLeft:
                    parent.left = TreeNode(value)
                else:
                    parent.right = TreeNode(value)
                return None

            if value < root.val:
                BST(value, root.left, root, True)
            elif value > root.val:
                BST(value, root.right, root, False)
        
        nodes = [root]
        next_level = None
        temp_root = TreeNode(root.val)

        while nodes:
            next_level = []
            for node in nodes:
                if node.left:
                    next_level.append(node.left)
                    BST(node.left.val, temp_root, temp_root)
                if node.right:
                    next_level.append(node.right)
                    BST(node.right.val, temp_root, temp_root)
            nodes = next_level
        
        return str(root) == str(temp_root)
        """

        # Print Tree
        """
        nodes2 = [temp_root]
        l = l2 = []
        output = [[temp_root.val]]
        while nodes2:
            l = []
            l2 = []
            for node in nodes2:
                if node.left:
                    l.append(node.left)
                    l2.append(node.left.val)
                if node.right:
                    l.append(node.right)
                    l2.append(node.right.val)
            nodes2 = l
            if l2:
                output.append(l2)
        print(output)
        """
