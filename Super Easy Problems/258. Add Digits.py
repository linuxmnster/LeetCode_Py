"""
🧩 Problem: 258. Add Digits
Given an integer num, repeatedly add its digits until the result has only one digit.
Example: 38 → 3 + 8 = 11 → 1 + 1 = 2
"""

class Solution:
    def addDigits(self, num: int) -> int:
        if num < 9:
            return num
        return 1 + (num - 1) % 9

"""EXPLANATION"""
"""
If num < 9, just return it (it's already a single digit).
Otherwise, use the digital root formula:
    
    The result of repeatedly adding digits reduces to:
    🔢 1 + (num - 1) % 9

This avoids loops or recursion and works in O(1) time.

🧠 Example:
Input: num = 38
→ 3 + 8 = 11 → 1 + 1 = 2
✔️ Formula: 1 + (38 - 1) % 9 = 1 + 37 % 9 = 1 + 1 = 2
"""

# Time Complexity : O(1)
# Space Complexity : O(1)