# 271. Encode and Decode Strings
### Tag: [Medium](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#medium-level), [Array](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#array), [String](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#string), [Design](https://github.com/TheOnlyMiki/LeetCode-For-Fun/tree/main#design)
---
Design an algorithm to encode a list of strings into a single string, send it over the network, and then decode it back into the original list of strings.

Implement `encode(strs)` and `decode(s)` so that `decode(encode(strs)) == strs`. The two functions must be stateless (no shared variables between calls), and must not rely on any built-in serialize methods.

**Example 1:**

```
Input: ["Hello", "World"]
Output: ["Hello", "World"]
```

**Example 2:**

```
Input: [""]
Output: [""]
```

**Constraints:**

- `0 <= strs.length < 100`
- `0 <= strs[i].length < 200`
- `strs[i]` contains any possible characters out of 256 valid ASCII characters.

> Premium problem on LeetCode. Statement above is paraphrased.

---

### Solution

```python
class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + "#" + s

        return output

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        while i < len(s):
            temp_i = i
            while s[temp_i] != '#':
                temp_i += 1

            n = int(s[i:temp_i])
            start_i = temp_i + 1
            end_i = start_i + n
            output.append(s[start_i:start_i+n])
            
            i = end_i

        return output
```

### Notes

**Idea: length prefix.** Each string is written as `<length>#<string>`, e.g. `["Hello", "World"]` becomes `5#Hello5#World`.

Why this is safe: a delimiter alone (like `,`) breaks when a string contains that delimiter. With a length prefix, the decoder reads digits up to the first `#`, then takes exactly `n` characters and **never inspects their content**. So a string like `"3#x"` is fine: the `#` inside it is just data. Empty strings work too (`0#`), and an empty list encodes to `""`.

**Complexity:** time O(N) where N is the total number of characters; space O(N) for the output.

**Small improvement:** repeated `output += ...` can be slow on some languages; in Python, collecting parts in a list and `"".join(parts)` is the more idiomatic way.
