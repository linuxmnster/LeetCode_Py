"""
🧩 Problem: 28. Find the Index of the First Occurrence in a String (a.k.a. strStr)
Given two strings haystack and needle, return the index of the first occurrence of needle in haystack.
If needle is not found, return -1.
If needle is empty, return 0.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


"""EXPLANATION"""
"""
First, check if needle is longer than haystack → If so, return -1 (can't find it).
Loop through all possible starting positions in haystack where needle could fit.

    Compare substring haystack[i : i + len(needle)] with needle.
    If they match, return i (the starting index of the match).

If the loop ends and no match is found, return -1.
"""

#Time Complexity: O(n * m)
#Space Complexity: O(1)