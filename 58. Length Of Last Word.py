"""
🧩 Problem: 58. Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is defined as a maximal substring consisting only of non-space characters.
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1
        while s[end] == " ":
            end -= 1
        
        srt = end
        while srt >= 0 and s[srt] != " ":
            srt -= 1
        return end - srt

"""EXPLANATION"""
"""
Start from the end of the string.
Skip any trailing spaces.
Then count backwards until you hit a space or reach the beginning — this marks the last word.
The length of the last word is end - srt.

🧠 Example:
Input: "Hello World "
Skip spaces → end = 10 → 9 → 8
Now, s[8] = 'd' (end of last word)
Move srt back until space: srt = 7 → 6 → 5 (s[5] = ' ')
Length = end - srt = 8 - 5 = 3
"""

# Time Complexity: O(n)
# Space Complexity: O(1)