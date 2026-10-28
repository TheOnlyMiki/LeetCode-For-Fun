# 49. Group Anagrams
### Tag: [Medium](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#medium-level), [Array](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#array), [Hash Table](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#hash-table), [String](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#string), [Sorting](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#sorting)
---
<div class="px-5 pt-4"><div class="flex"></div><div class="_1l1MA" data-track-load="description_content"><p>Given an array of strings <code>strs</code>, group <strong>the anagrams</strong> together. You can return the answer in <strong>any order</strong>.</p>

<p>An <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> strs = ["eat","tea","tan","ate","nat","bat"]
<strong>Output:</strong> [["bat"],["nat","tan"],["ate","eat","tea"]]
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> strs = [""]
<strong>Output:</strong> [[""]]
</pre><p><strong class="example">Example 3:</strong></p>
<pre><strong>Input:</strong> strs = ["a"]
<strong>Output:</strong> [["a"]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= strs.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= strs[i].length &lt;= 100</code></li>
	<li><code>strs[i]</code> consists of lowercase English letters.</li>
</ul>
</div></div>

---
<img src="Submit.png" width="700" height="215" />

### Solution

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        record = defaultdict(list)

        # Method 1
        """
        for word in strs:
            temp = "".join(sorted(word))
            '''
            if temp in record:
                record[temp].append(word)
            else:
                record[temp] = [word]'''
            #record[temp] = record.get(temp, []) + [word]

            record[temp].append(word)
        """
        # time complexity O(n mlogm), space complexity O(n m)

        # Method 2
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1

            record[tuple(count)].append(word)

        return list(record.values())
        # time complexity O(n m), space complexity O(n)
```
