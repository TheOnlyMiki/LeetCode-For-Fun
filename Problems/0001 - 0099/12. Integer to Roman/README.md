# 12. Integer to Roman
### Tag: [Medium](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#medium-level), [Hash Table](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#hash-table), [Math](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#math), [String](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#string)
---
<div class="px-5 pt-4"><div class="flex"></div><div class="_1l1MA" data-track-load="description_content"><p>Roman numerals are represented by seven different symbols:&nbsp;<code>I</code>, <code>V</code>, <code>X</code>, <code>L</code>, <code>C</code>, <code>D</code> and <code>M</code>.</p>

<pre><strong>Symbol</strong>       <strong>Value</strong>
I             1
V             5
X             10
L             50
C             100
D             500
M             1000</pre>

<p>For example,&nbsp;<code>2</code> is written as <code>II</code>&nbsp;in Roman numeral, just two one's added together. <code>12</code> is written as&nbsp;<code>XII</code>, which is simply <code>X + II</code>. The number <code>27</code> is written as <code>XXVII</code>, which is <code>XX + V + II</code>.</p>

<p>Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not <code>IIII</code>. Instead, the number four is written as <code>IV</code>. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as <code>IX</code>. There are six instances where subtraction is used:</p>

<ul>
	<li><code>I</code> can be placed before <code>V</code> (5) and <code>X</code> (10) to make 4 and 9.&nbsp;</li>
	<li><code>X</code> can be placed before <code>L</code> (50) and <code>C</code> (100) to make 40 and 90.&nbsp;</li>
	<li><code>C</code> can be placed before <code>D</code> (500) and <code>M</code> (1000) to make 400 and 900.</li>
</ul>

<p>Given an integer, convert it to a roman numeral.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> num = 3
<strong>Output:</strong> "III"
<strong>Explanation:</strong> 3 is represented as 3 ones.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> num = 58
<strong>Output:</strong> "LVIII"
<strong>Explanation:</strong> L = 50, V = 5, III = 3.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> num = 1994
<strong>Output:</strong> "MCMXCIV"
<strong>Explanation:</strong> M = 1000, CM = 900, XC = 90 and IV = 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 3999</code></li>
</ul>
</div></div>

---
<img src="Submit.png" width="700" height="215" />

### Solution

```python
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        number = {  0 : '',
                    1 : 'I',
                    5 : 'V',
                    10 : 'X',
                    50 : 'L',
                    100 : 'C',
                    500 : 'D',
                    1000 : 'M',
                    4 : "VI",
                    9 : "XI",
                    40 : "LX",
                    90 : "CX",
                    400 : "DC",
                    900 : "MC"  }

        roman = ""

        for i, v in enumerate(str(num)[::-1]):
            value = int(v)
            c_represend = 10**i
            over_5 = False

            if value > 5 and value != 9:
                over_5 = True
                value = value % 5

            represend = value * c_represend

            if represend in number:
                roman += number[represend]
            else:
                for _ in range(value):
                    roman += number[c_represend]

            if over_5:
                roman += number[5*c_represend]

        return roman[::-1]
```
