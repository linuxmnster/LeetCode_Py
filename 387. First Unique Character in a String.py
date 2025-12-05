"""🧩 Problem: 387. First Unique Character in a String

Given a string s, find the first non-repeating character and return its index.
If it does not exist, return -1.

A character is considered unique if it appears exactly once in the string."""

"""💡 Solution"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        frq = {}
        for i in s:
            frq[i] = frq.get(i, 0) + 1
        
        for i, c in enumerate(s):
            if frq[c] == 1:
                return i
        return -1

"""🧠 EXPLANATION
Step 1 — Count frequencies

We use a dictionary frq to store how many times each character appears.

Example:
s = "leetcode"
frq = { 'l':1, 'e':3, 't':1, 'c':1, 'o':1, 'd':1 }

Step 2 — Find the first character with frequency 1

Loop again through the string with index:

When we check characters in order (l → e → e → t…)

The first one whose count is 1 is the answer.

For "leetcode" → 'l' appears once → index 0

If no character has frequency 1, return -1.

📘 Example

Input:

s = "loveleetcode"


Frequency table:

l:2, o:2, v:1, e:4, t:1, c:1, d:1


Scan in order:

l → freq 2 → skip

o → freq 2 → skip

v → freq 1 → return index 2

Output:

2

⏱️ TIME COMPLEXITY: O(n)

First loop → count frequencies → O(n)

Second loop → find first unique → O(n)
Total = O(n)

🧠 SPACE COMPLEXITY: O(1)

Why O(1)?
The dictionary can store max 26 lowercase letters, so it never grows with input size → constant space."""