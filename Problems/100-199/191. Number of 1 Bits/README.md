# 191. Number of 1 Bits
### Tag: [Easy](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#easy-level), [Divide and Conquer](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#divide-and-conquer), [Bit Manipulation](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#bit-manipulation)
---
<div class="px-5 pt-4"><div class="flex"></div><div class="xFUwe" data-track-load="description_content"><p>Write a function that takes&nbsp;the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the <a href="http://en.wikipedia.org/wiki/Hamming_weight" target="_blank">Hamming weight</a>).</p>

<p><strong>Note:</strong></p>

<ul>
	<li>Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.</li>
	<li>In Java, the compiler represents the signed integers using <a href="https://en.wikipedia.org/wiki/Two%27s_complement" target="_blank">2's complement notation</a>. Therefore, in <strong class="example">Example 3</strong>, the input represents the signed integer. <code>-3</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> n = 00000000000000000000000000001011
<strong>Output:</strong> 3
<strong>Explanation:</strong> The input binary string <strong>00000000000000000000000000001011</strong> has a total of three '1' bits.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> n = 00000000000000000000000010000000
<strong>Output:</strong> 1
<strong>Explanation:</strong> The input binary string <strong>00000000000000000000000010000000</strong> has a total of one '1' bit.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> n = 11111111111111111111111111111101
<strong>Output:</strong> 31
<strong>Explanation:</strong> The input binary string <strong>11111111111111111111111111111101</strong> has a total of thirty one '1' bits.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The input must be a <strong>binary string</strong> of length <code>32</code>.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> If this function is called many times, how would you optimize it?</div></div>

---
<img src="Submit.png" width="700" height="215" />

### Solution

```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        devide = (n, n)
        count = 0
        while devide[0] != 0:
            devide = divmod(devide[0], 2)
            if devide[1] == 1:
                count += 1

        return count
```
