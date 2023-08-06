# 2. Add Two Numbers
### Tag: [Medium](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#medium-level), [Linked List](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#linked-list), [Math](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#math)
---
<div class="px-5 pt-4"><div class="flex"></div><div class="_1l1MA" data-track-load="description_content"><p>You are given two <strong>non-empty</strong> linked lists representing two non-negative integers. The digits are stored in <strong>reverse order</strong>, and each of their nodes contains a single digit. Add the two numbers and return the sum&nbsp;as a linked list.</p>

<p>You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg" style="width: 483px; height: 342px;">
<pre><strong>Input:</strong> l1 = [2,4,3], l2 = [5,6,4]
<strong>Output:</strong> [7,0,8]
<strong>Explanation:</strong> 342 + 465 = 807.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> l1 = [0], l2 = [0]
<strong>Output:</strong> [0]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
<strong>Output:</strong> [8,9,9,9,0,0,0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in each linked list is in the range <code>[1, 100]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
	<li>It is guaranteed that the list represents a number that does not have leading zeros.</li>
</ul>
</div></div>

---
<img src="Submit.png" width="700" height="215" />

### Solution

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Option 2 - string operations in python
        """
        head = ListNode()
        record = head

        num = num_2 = ""

        while l1 or l2:
            if l1:
                num += str(l1.val)
                l1 = l1.next
            if l2:
                num_2 += str(l2.val)
                l2 = l2.next

        num = int(num[::-1])
        num_2 = int(num_2[::-1])

        consum = str(num + num_2)[::-1]

        for i in range(len(consum)-1):
            record.val = int(consum[i])
            record.next = ListNode()
            record = record.next

        record.val = int(consum[-1])

        return head
        """

        # Option 1
        head = ListNode()
        record = head
        consum = None
        carry = 0

        while l1 or l2:
            if l1 and l2:
                consum = l1.val + l2.val + carry
                record.next = (ListNode(consum%10) if consum > 9 else ListNode(consum))
                carry = (1 if consum > 9 else 0)
                l1 = l1.next
                l2 = l2.next
            else:
                if l1:
                    consum = l1.val + carry
                    record.next = (ListNode(consum%10) if consum > 9 else ListNode(consum))
                    carry = (1 if consum > 9 else 0)
                    l1 = l1.next
                else:
                    consum = l2.val + carry
                    record.next = (ListNode(consum%10) if consum > 9 else ListNode(consum))
                    carry = (1 if consum > 9 else 0)
                    l2 = l2.next

            record = record.next

        if carry == 1:
            record.next = ListNode(carry)

        return head.next
```
