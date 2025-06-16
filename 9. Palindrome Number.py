"""
🧩 Problem: 9. Palindrome Number
Determine whether an integer x is a palindrome.
A palindrome number reads the same backward as forward (e.g., 121, 1331).
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        rev  = 0
        y = x
        while y:
            rev = rev * 10 + y % 10
            y = y // 10
        return rev == x
    
"""EXPLANATION"""
"""
If x is negative → return False (e.g., -121 is not a palindrome because of the minus sign).
Make a copy of x in y, and reverse it digit by digit:
    Multiply rev by 10 and add the last digit of y.
    Remove the last digit from y using integer division (// 10).

Finally, compare the reversed number rev with the original number x.

🧠 Example:
Input: x = 121

Initial: rev = 0, y = 121

Step 1: rev = 0 * 10 + 1 = 1, y = 12

Step 2: rev = 1 * 10 + 2 = 12, y = 1

Step 3: rev = 12 * 10 + 1 = 121, y = 0

Now rev == x → ✅ return True
"""
