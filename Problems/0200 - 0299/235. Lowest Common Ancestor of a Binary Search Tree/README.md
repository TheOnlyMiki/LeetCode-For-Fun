# 235. Lowest Common Ancestor of a Binary Search Tree
### Tag: [Medium](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#medium-level), [Depth-First Search](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#depth-first-search), [Binary Search](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#binary-search), [Binary Tree](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#binary-tree)
---
<div class="px-5 pt-4"><div class="flex"></div><div class="xFUwe" data-track-load="description_content"><p>Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.</p>

<p>According to the <a href="https://en.wikipedia.org/wiki/Lowest_common_ancestor" target="_blank">definition of LCA on Wikipedia</a>: “The lowest common ancestor is defined between two nodes <code>p</code> and <code>q</code> as the lowest node in <code>T</code> that has both <code>p</code> and <code>q</code> as descendants (where we allow <strong>a node to be a descendant of itself</strong>).”</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png" style="width: 200px; height: 190px;">
<pre><strong>Input:</strong> root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
<strong>Output:</strong> 6
<strong>Explanation:</strong> The LCA of nodes 2 and 8 is 6.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png" style="width: 200px; height: 190px;">
<pre><strong>Input:</strong> root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> root = [2,1], p = 2, q = 1
<strong>Output:</strong> 2
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[2, 10<sup>5</sup>]</code>.</li>
	<li><code>-10<sup>9</sup> &lt;= Node.val &lt;= 10<sup>9</sup></code></li>
	<li>All <code>Node.val</code> are <strong>unique</strong>.</li>
	<li><code>p != q</code></li>
	<li><code>p</code> and <code>q</code> will exist in the BST.</li>
</ul>
</div></div>

---
<img src="Submit.png" width="700" height="215" />

### Solution

```python
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
        # Option 3
        """
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
        """

        # Option 2
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

        # Option 1 - BST feature to solved
        maximum, minimum = (p.val, q.val) if p.val > q.val else (q.val, p.val)

        while root:
            if root.val > maximum:
                root = root.left
            elif root.val < minimum:
                root = root.right
            else:
                return root

        return root

        """
        def dfs(node):
            if node:
                if node.val > maximum:
                    dfs(node.left)
                elif node.val < minimum:
                    dfs(node.right)
                else:
                    self.output = node

            return

        self.output = None
        dfs(root)
        return self.output
        """
```
