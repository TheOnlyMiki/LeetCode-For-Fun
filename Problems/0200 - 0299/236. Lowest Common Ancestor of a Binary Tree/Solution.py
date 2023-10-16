# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Option 2
        self.output = None

        def dfs(root):
            if not root:
                return False, False

            find_p, find_q = dfs(root.left)
            if find_p and find_q:
                return True, True

            find2_p, find2_q = dfs(root.right)
            if find2_p and find2_q:
                return True, True

            find_p = (True if find2_p else find_p)
            find_q = (True if find2_q else find_q)

            if find_p and find_q:
                self.output = root
                return True, True

            find_p = (True if root.val == p.val else find_p )
            find_q = (True if root.val == q.val else find_q )
            if find_p and find_q:
                self.output = root
                return True, True

            return find_p, find_q

        dfs(root)

        return self.output

        # Option 1
        """
        def dfs(root, path):
            if root:
                if self.p_path and self.q_path:
                    return

                if root.val == p.val:
                    self.p_path = path + [root.val]
                elif root.val == q.val:
                    self.q_path = path + [root.val]

                path.append(root.val)
                dfs(root.left, path)
                dfs(root.right, path)
                path.pop()
            
            return
            
        self.p_path = None
        self.q_path = None
        dfs(root, [])

        for i in range(min(len(self.p_path), len(self.q_path))):
            if self.p_path[i] != self.q_path[i]:
                return root
            elif root.left and root.left.val == self.p_path[i]:
                root = root.left
            elif root.right and root.right.val == self.p_path[i]:
                root = root.right

        return root
        """
