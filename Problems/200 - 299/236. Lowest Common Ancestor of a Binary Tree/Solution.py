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

        def bfs(root):
            if not root:
                return False, False

            find_p, find_q = bfs(root.left)
            if find_p and find_q:
                return True, True

            find2_p, find2_q = bfs(root.right)
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

        bfs(root)

        return self.output

        # Option 1 - too slow
        """
        self.p_path = None
        self.q_path = None

        def bfs(root, path):
            if not root:
                return None

            if root.val == p.val:
                self.p_path = (path + ',' + str(p.val)).split(',')
            elif root.val == q.val:
                self.q_path = (path + ',' + str(q.val)).split(',')

            bfs(root.left, path + ',' + str(root.val))
            bfs(root.right, path + ',' + str(root.val))

        bfs(root, "")

        i = 1
        length = min(len(self.p_path), len(self.q_path))
        temp = None
        
        while i < length and self.p_path[i] == self.q_path[i]:
            temp = int(self.p_path[i])
            if root.left and root.left.val == temp:
                root = root.left
            elif root.right and root.right.val == temp:
                root = root.right
            i += 1

        return root
        """
