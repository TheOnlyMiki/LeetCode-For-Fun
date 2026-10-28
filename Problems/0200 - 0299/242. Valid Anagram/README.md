# 242. Valid Anagram
### Tag: [Easy](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#easy-level), [Hash Table](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#hash-table), [String](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#string), [Sorting](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#sorting)
---
<div class="px-5 pt-4"><div class="flex"></div><div class="_1l1MA" data-track-load="description_content"><p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code> <em>if</em> <code>t</code> <em>is an anagram of</em> <code>s</code><em>, and</em> <code>false</code> <em>otherwise</em>.</p>

<p>An <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "anagram", t = "nagaram"
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "rat", t = "car"
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> What if the inputs contain Unicode characters? How would you adapt your solution to such a case?</p>
</div></div>

---
<img src="Submit.png" width="700" height="215" />

### Solution

```python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        '''
        s = s.decode()
        t = t.decode()

        count_s = {}
        count_t = {}

        try:
            for i in range(max(len(s), len(t))):
                if s[i] in count_s:
                    count_s[s[i]] += 1
                else:
                    count_s[s[i]] = 1

                if t[i] in count_t:
                    count_t[t[i]] += 1
                else:
                    count_t[t[i]] = 1
        except:
            return False

        return count_s == count_t
        '''

        
        if len(s) != len(t):
            return False

        # Method 1 - time complexity O(n), space complexity O(s+t)
        '''
        count_s, count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1

        return count_s == count_t'''

        # Method 2 - time complexity O(n logn), space complexity O(1) or O(s+t)
        '''return sorted(s) == sorted(t)
        '''

        # Method 3 - time complexity O(n + m), space complexity O(1)
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for n in count:
            if n != 0:
                return False
        return True
```
数组为什么比哈希表快： 两者都是 O(n)，差别在常数因子：
不用算哈希：数组用 ord(c) - ord('a') 直接得到下标；哈希表每次存取都要先算 hash，再处理可能的冲突。
内存连续：26 个 int 挨在一起，基本都在 CPU 缓存里；哈希表的桶分散在内存各处，缓存命中率低。
比较更便宜：两个长度 26 的数组逐位比较，固定 26 次；比较两个哈希表要遍历键、逐个查找。
空间固定：数组永远是 26 格，算 O(1)；哈希表按实际字符数增长，还会预留空位。

在 Python 里，Counter 是用 C 实现的，手写 for 循环操作 list 反而可能更慢。不一定是 Python 实测更快。用 C++/Java 写时，差别才明显。
