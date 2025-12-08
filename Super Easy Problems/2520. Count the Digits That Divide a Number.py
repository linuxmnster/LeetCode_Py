"""
🧩 Problem: 2520. Count the Digits That Divide a Number

Given an integer num, return the number of digits in num that divide num evenly.
A digit d divides num evenly if:num % d == 0
"""

class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        temp = num
        while temp > 0:
            r = temp % 10      # extract last digit
            if num % r == 0:   # check if digit divides num
                count += 1
            temp = temp // 10  # remove last digit
        return count

"""🧠 EXPLANATION

We want to check each digit of num individually.

Steps:
Copy num to a temporary variable temp.
Loop while temp > 0:
Extract the last digit r = temp % 10.
If the digit divides the number (num % r == 0), increment count.
Remove the last digit (temp = temp // 10).
Return the final count.

Example
Input:
num = 1248

Digits: 8, 4, 2, 1
Check each:

Digit	num % digit	Divides?
8	0	Yes
4	0	Yes
2	0	Yes
1	0	Yes
Total digits that divide → 4

Output:
4

⏱️ TIME COMPLEXITY: O(d)
Where d = number of digits in num (at most 10 digits for constraint).
Very efficient.

🧠 SPACE COMPLEXITY: O(1)
Only a few variables are used → constant space."""