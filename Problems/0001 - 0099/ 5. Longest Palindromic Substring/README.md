# 5. Longest Palindromic Substring
### Tag: [Medium](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#medium-level), [String](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#string), [Dynamic Programming](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#dynamic-programming)
---
<div class="px-5 pt-4"><div class="flex"></div><div class="xFUwe" data-track-load="description_content"><p>Given a string <code>s</code>, return <em>the longest</em> <span data-keyword="palindromic-string" datakeyword="palindromic-string" class=" cursor-pointer relative text-dark-blue-s text-sm"><div class="popover-wrapper inline-block" data-headlessui-state=""><div><div id="headlessui-popover-button-:r16:" aria-expanded="false" data-headlessui-state=""><div><em>palindromic</em></div></div><div style="position: fixed; z-index: 9999; inset: 0px auto auto 0px; transform: translate(284px, 221px);"></div></div></div></span> <span data-keyword="substring-nonempty" datakeyword="substring-nonempty" class=" cursor-pointer relative text-dark-blue-s text-sm"><div class="popover-wrapper inline-block" data-headlessui-state=""><div><div id="headlessui-popover-button-:r19:" aria-expanded="false" data-headlessui-state=""><div><em>substring</em></div></div><div style="position: fixed; z-index: 9999; inset: 0px auto auto 0px; transform: translate(351px, 221px);"></div></div></div></span> in <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "babad"
<strong>Output:</strong> "bab"
<strong>Explanation:</strong> "aba" is also a valid answer.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "cbbd"
<strong>Output:</strong> "bb"
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consist of only digits and English letters.</li>
</ul>
</div></div>

---
<img src="Submit.png" width="700" height="215" />

### Solution

```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length < 2:
            return s

        def checkPalindrome(left, right):
            while left > -1 and right < length and s[left] == s[right]:
                left -= 1
                right += 1

            return (left+1, right)

        record = (None, None)
        record_length = temp1 = temp2 = 0

        for i in range(length):
            temp1 = checkPalindrome(i, i)
            temp2 = checkPalindrome(i, i+1)
            
            temp1 = (temp2, temp2[1] - temp2[0]) if temp2[1] - temp2[0] > temp1[1] - temp1[0] else (temp1, temp1[1] - temp1[0])
            if temp1[1] > record_length:
                record_length = temp1[1]
                record = temp1[0]
        
        return s[record[0] : record[1]]
```
