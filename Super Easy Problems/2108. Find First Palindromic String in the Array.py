"""---
# 🧩 Problem: **2108. Find First Palindromic String in the Array**

You are given an array of strings `words`.
Return the **first string** in the array that is a **palindrome**.

A string is a *palindrome* if it reads the same forward and backward.
If **no palindromic string** exists, return an empty string `""`.
---"""

class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        def isPalindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        
        for i in words:
            if isPalindrome(i):
                return i
        return ""
"""```

---

## 🧠 **EXPLANATION**

### Helper Function: `isPalindrome(s)`

Checks a string using two pointers:

* `l` starts at the left
* `r` starts at the right
* Move inward while comparing characters
* If characters mismatch → not a palindrome
* If all match → palindrome

### Main Logic:

Loop through each word in `words`:

* For each word, call `isPalindrome()`
* Return the **first** word that is a palindrome
* If none found, return `""`

---

## 📘 **Example**

Input:
words = ["abc","car","ada","racecar","cool"]

Check order:
* "abc" → not palindrome
* "car" → not palindrome
* "ada" → palindrome → return `"ada"`

Output:
"ada"
---

## ⏱️ **TIME COMPLEXITY: O(n * m)**
Where:
* `n` = number of words
* `m` = average length of each word
  Each word is checked using a two-pointer scan.
---

## 🧠 **SPACE COMPLEXITY: O(1)**
Only pointers and variables used, no extra data structures.

---"""
"""
we can also use the code
for i in words:
    if i == i[::-1]:
        return i
return ""

but for this code the time complexity will be O(N*M) same as the above
but the space complexity will be O(N) as the reverse of the string has to be stored
"""