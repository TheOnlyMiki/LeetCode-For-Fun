# 430. Flatten a Multilevel Doubly Linked List
### Tag: [Medium](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#medium-level), [Linked List](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#linked-list), [Depth-First Search](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#depth-first-search), [Stack](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#stack)
---
<div class="px-5 pt-4"><div class="flex"></div><div class="xFUwe" data-track-load="description_content"><p>You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional <strong>child pointer</strong>. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a <strong>multilevel data structure</strong> as shown in the example below.</p>

<p>Given the <code>head</code> of the first level of the list, <strong>flatten</strong> the list so that all the nodes appear in a single-level, doubly linked list. Let <code>curr</code> be a node with a child list. The nodes in the child list should appear <strong>after</strong> <code>curr</code> and <strong>before</strong> <code>curr.next</code> in the flattened list.</p>

<p>Return <em>the </em><code>head</code><em> of the flattened list. The nodes in the list must have <strong>all</strong> of their child pointers set to </em><code>null</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/09/flatten11.jpg" style="width: 700px; height: 339px;">
<pre><strong>Input:</strong> head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
<strong>Output:</strong> [1,2,3,7,8,11,12,9,10,4,5,6]
<strong>Explanation:</strong> The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:
<img src="https://assets.leetcode.com/uploads/2021/11/09/flatten12.jpg" style="width: 1000px; height: 69px;">
</pre>

<p><strong class="example">Example 2:</strong></p>
<img src="flatten21.jpg" style="width: 200px; height: 200px;">
<pre><strong>Input:</strong> head = [1,2,null,3]
<strong>Output:</strong> [1,3,2]
<strong>Explanation:</strong> The multilevel linked list in the input is shown.
After flattening the multilevel linked list it becomes:
<img src="https://assets.leetcode.com/uploads/2021/11/24/list.jpg" style="width: 300px; height: 87px;">
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> head = []
<strong>Output:</strong> []
<strong>Explanation:</strong> There could be empty list in the input.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of Nodes will not exceed <code>1000</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>How the multilevel linked list is represented in test cases:</strong></p>

<p>We use the multilevel linked list from <strong class="example">Example 1</strong> above:</p>

<pre> 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL</pre>

<p>The serialization of each level is as follows:</p>

<pre>[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
</pre>

<p>To serialize all levels together, we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:</p>

<pre>[1,    2,    3, 4, 5, 6, null]
             |
[null, null, 7,    8, 9, 10, null]
                   |
[            null, 11, 12, null]
</pre>

<p>Merging the serialization of each level and removing trailing nulls we obtain:</p>

<pre>[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
</pre>
</div></div>

---
<img src="Submit.png" width="700" height="215" />

### Solution

```python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # Option 2 - Stack
        if not head:
            return None

        record = []
        if head.next:
            record.append(head.next)
        if head.child:
            record.append(head.child)
            head.child = None

        prev = head
        while record:
            node = record.pop()

            if node.next:
                record.append(node.next)
            if node.child:
                record.append(node.child)
                node.child = None

            node.prev, prev.next, prev = prev, node, node

        return head

        # Option 1 - DFS
        """
        def dfs(node):
            if node:
                if node.child:
                    temp = node.next
                    node.next, node.child.prev, node.child = node.child, node, None
                    node = dfs(node.next)
                    node.next = temp
                    if temp:
                        temp.prev = node

                return dfs(node.next) if node.next else node

            return

        dfs(head)

        '''
        cur = head
        o = []
        while cur:
            print("current",cur.val)
            if cur.child:
                print("child",cur.child.val)
            if cur.prev:
                print("prev",cur.prev.val)
            if cur.next:
                print("next",cur.next.val)

            print()
            o.append(cur.val)
            cur = cur.next

        print(o)
        '''

        return head
        """
```
